"""
Tests for AEI Cryptography Module

Tests cryptographic systems based on the indeterminate algebra:
- Paired-prime square root cryptography
- Indeterminate modular arithmetic
- I-matrix encryption
- Watermark detection
"""

import pytest
from ialgebra.cryptography import (
    PairedPrime,
    IndeterminateModularArithmetic,
    IndeterminateMatrix,
    PairedPrimeCryptosystem,
    watermark_detection,
    visualize_crypto_state,
    NEON_COLORS
)


class TestPairedPrime:
    """Test paired-prime cryptographic primitives."""
    
    def test_paired_prime_creation(self):
        """Test creating paired-prime structure."""
        pair = PairedPrime(value=17, pair_partner=19)
        assert pair.value == 17
        assert pair.pair_partner == 19
    
    def test_paired_product(self):
        """Test paired product calculation."""
        pair = PairedPrime(value=17, pair_partner=19)
        product = pair.paired_product()
        assert product == 17 * 19
        assert product == 323
    
    def test_even_prime_root_detection(self):
        """Test even-prime-like root detection."""
        # Pairs whose product has even-prime-like roots
        pair1 = PairedPrime(value=2, pair_partner=8)
        assert pair1.reveals_even_prime_root() is True  # 16 % 4 == 0
        
        pair2 = PairedPrime(value=3, pair_partner=5)
        assert pair2.reveals_even_prime_root() is False  # 15 % 4 != 0
    
    def test_cryptographic_key_component(self):
        """Test key component generation."""
        pair = PairedPrime(value=17, pair_partner=19)
        key_comp = pair.cryptographic_key_component()
        
        # Should produce deterministic key based on relationship
        assert key_comp > 0
        
        # Same pair should give same key
        pair2 = PairedPrime(value=17, pair_partner=19)
        assert pair2.cryptographic_key_component() == key_comp


class TestIndeterminateModularArithmetic:
    """Test modular arithmetic with I-components."""
    
    def test_modular_creation(self):
        """Test creating I-modular system."""
        mod = IndeterminateModularArithmetic(modulus=97)
        assert mod.modulus == 97
    
    def test_addition_without_i(self):
        """Test classical addition."""
        mod = IndeterminateModularArithmetic(modulus=97)
        result, has_i = mod.add_with_I(50, 60, has_I_a=False, has_I_b=False)
        
        assert result == (50 + 60) % 97
        assert has_i is False
    
    def test_addition_with_i_absorption(self):
        """Test I-absorption in addition."""
        mod = IndeterminateModularArithmetic(modulus=97)
        
        # If either has I, result has I
        result, has_i = mod.add_with_I(50, 60, has_I_a=True, has_I_b=False)
        assert has_i is True
        
        result, has_i = mod.add_with_I(50, 60, has_I_a=False, has_I_b=True)
        assert has_i is True
    
    def test_multiplication_with_i(self):
        """Test multiplication with I-components."""
        mod = IndeterminateModularArithmetic(modulus=97)
        
        # I * I = I (idempotency)
        result, has_i = mod.multiply_with_I(10, 20, has_I_a=True, has_I_b=True)
        assert has_i is True
    
    def test_inverse_without_i(self):
        """Test multiplicative inverse."""
        mod = IndeterminateModularArithmetic(modulus=97)
        
        # 42 * inverse = 1 (mod 97)
        inv = mod.inverse_with_I(42, has_I=False)
        assert inv is not None
        
        inv_val, inv_has_i = inv
        assert inv_has_i is False
        assert (42 * inv_val) % 97 == 1
    
    def test_i_has_no_inverse(self):
        """Test that I has no multiplicative inverse (P14 axiom)."""
        mod = IndeterminateModularArithmetic(modulus=97)
        
        # I has no inverse
        inv = mod.inverse_with_I(42, has_I=True)
        assert inv is None


class TestIndeterminateMatrix:
    """Test matrices with I-valued entries."""
    
    def test_matrix_creation(self):
        """Test creating I-matrix."""
        matrix = IndeterminateMatrix(size=2, modulus=97)
        assert matrix.size == 2
        assert matrix.modulus == 97
    
    def test_matrix_randomization(self):
        """Test randomizing matrix with I-components."""
        matrix = IndeterminateMatrix(size=2, modulus=97)
        matrix.randomize(I_probability=0.5)
        
        # Should have some I-components
        has_any_i = any(
            matrix.has_I[i][j]
            for i in range(matrix.size)
            for j in range(matrix.size)
        )
        # With 50% probability and 4 entries, very likely to have at least one I
        # (Not guaranteed, but extremely likely)
    
    def test_determinant_calculation(self):
        """Test determinant with I-tracking."""
        matrix = IndeterminateMatrix(size=2, modulus=97)
        
        # Set specific values
        matrix.real_part = [[2, 3], [5, 7]]
        matrix.has_I = [[False, False], [False, False]]
        
        det_val, has_i = matrix.determinant_signature()
        
        # det = 2*7 - 3*5 = 14 - 15 = -1 ≡ 96 (mod 97)
        assert det_val == 96
        assert has_i is False
    
    def test_determinant_with_i_propagation(self):
        """Test that I propagates through determinant."""
        matrix = IndeterminateMatrix(size=2, modulus=97)
        
        matrix.real_part = [[2, 3], [5, 7]]
        matrix.has_I = [[True, False], [False, False]]
        
        det_val, has_i = matrix.determinant_signature()
        assert has_i is True  # I propagates
    
    def test_vector_encryption(self):
        """Test encrypting vector with I-matrix."""
        matrix = IndeterminateMatrix(size=2, modulus=97)
        matrix.randomize(I_probability=0.3)
        
        plaintext = [42, 58]
        ciphertext = matrix.encrypt_vector(plaintext)
        
        assert len(ciphertext) == 2
        # Each entry is (value, has_I) tuple
        assert all(isinstance(entry, tuple) for entry in ciphertext)
        assert all(len(entry) == 2 for entry in ciphertext)


class TestPairedPrimeCryptosystem:
    """Test complete paired-prime cryptosystem."""
    
    def test_cryptosystem_creation(self):
        """Test creating cryptosystem."""
        crypto = PairedPrimeCryptosystem(security_parameter=64)
        assert crypto.security_bits == 64
        assert crypto.key_generated is False
    
    def test_key_generation(self):
        """Test keypair generation."""
        crypto = PairedPrimeCryptosystem(security_parameter=64)
        public, private = crypto.generate_keypair()
        
        assert crypto.key_generated is True
        assert public is not None
        assert private is not None
        
        # Public key: (n, e)
        n, e = public
        assert n > 0
        assert e == 65537  # Standard public exponent
        
        # Private key: two PairedPrime objects
        pair1, pair2 = private
        assert isinstance(pair1, PairedPrime)
        assert isinstance(pair2, PairedPrime)
    
    def test_encryption_decryption(self):
        """Test encrypt/decrypt roundtrip."""
        crypto = PairedPrimeCryptosystem(security_parameter=64)
        crypto.generate_keypair()
        
        message = 123456
        ciphertext = crypto.encrypt(message)
        decrypted = crypto.decrypt(ciphertext)
        
        assert decrypted == message
    
    def test_signature_verification(self):
        """Test sign/verify roundtrip."""
        crypto = PairedPrimeCryptosystem(security_parameter=64)
        crypto.generate_keypair()
        
        message = 789012
        signature = crypto.sign(message)
        
        # Verify signature
        is_valid = crypto.verify(message, signature)
        assert is_valid is True
        
        # Wrong message should fail
        is_valid_wrong = crypto.verify(message + 1, signature)
        assert is_valid_wrong is False
    
    def test_different_keys_different_ciphertext(self):
        """Test that different keys produce different encryption."""
        message = 111111
        
        crypto1 = PairedPrimeCryptosystem(security_parameter=64)
        crypto1.generate_keypair()
        cipher1 = crypto1.encrypt(message)
        
        crypto2 = PairedPrimeCryptosystem(security_parameter=64)
        crypto2.generate_keypair()
        cipher2 = crypto2.encrypt(message)
        
        # Different keys should give different ciphertext
        # (Extremely unlikely to be same)
        assert cipher1 != cipher2


class TestWatermarkDetection:
    """Test AEI mathematical watermark detection."""
    
    def test_detect_aei_signature(self):
        """Test detecting AEI-derived data."""
        # Create data with paired-prime signatures
        data = bytes([16, 32, 48, 64, 80, 96, 112, 128])  # All divisible by 4
        
        has_watermark = watermark_detection(data)
        # Should detect signature (many products % 4 == 0)
        assert has_watermark is True
    
    def test_no_signature_in_random(self):
        """Test that random data has no signature."""
        # Random-like data without structure
        data = bytes([1, 3, 5, 7, 11, 13, 17, 19])  # Odd numbers
        
        has_watermark = watermark_detection(data)
        # Should not detect signature
        assert has_watermark is False


class TestVisualization:
    """Test neon visualization functions."""
    
    def test_neon_colors_defined(self):
        """Test that neon color palette exists."""
        assert 'cyan' in NEON_COLORS
        assert 'purple' in NEON_COLORS
        assert 'lime' in NEON_COLORS
        assert 'red' in NEON_COLORS
        
        # Colors should be hex strings
        assert NEON_COLORS['cyan'].startswith('#')
        assert len(NEON_COLORS['cyan']) == 7
    
    def test_visualize_crypto_state(self):
        """Test crypto state visualization."""
        # High security with I
        color = visualize_crypto_state(has_I=True, security_level=0.9)
        assert color == NEON_COLORS['lime']  # Paired-prime secured
        
        # Low security with I
        color = visualize_crypto_state(has_I=True, security_level=0.3)
        assert color == NEON_COLORS['orange']  # Warning
        
        # Low security without I
        color = visualize_crypto_state(has_I=False, security_level=0.3)
        assert color == NEON_COLORS['red']  # Insecure
        
        # High security without I
        color = visualize_crypto_state(has_I=False, security_level=0.9)
        assert color == NEON_COLORS['purple']  # J-field secured


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
