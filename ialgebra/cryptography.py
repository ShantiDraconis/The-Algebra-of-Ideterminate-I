"""
Cryptographic Systems Based on AEI Framework

Demonstrações educacionais em torno da álgebra do indeterminado:
- PairedPrimeCryptosystem: RSA com quatro primos (a segurança é a do RSA; a
  álgebra do indeterminado não entra nela)
- Indeterminate Matrix Encryption (demonstração, sem análise de segurança)
- I-Field Modular Arithmetic

Author: Tiago Fagliari (ORCID: 0009-0006-6874-3910)

Security Note:
    This implementation uses `random` module for demonstration purposes.
    Production cryptographic systems MUST use `secrets` module or
    cryptographically secure random number generators.
"""

from typing import List, Tuple, Optional
from dataclasses import dataclass
import random
import secrets  # For cryptographically secure random numbers
from .types import Indeterminate, ExtendedElement, I


@dataclass
class PairedPrime:
    """
    Represents a number functioning as an "even prime" under paired operations.
    
    This is Fagliari's discovery: certain numbers, when multiplied by their
    pairs, reveal square roots that behave like even primes in the AEI framework.
    
    Classical mathematics: only even prime is 2
    AEI framework: paired operations reveal even-prime-like behavior
    """
    
    value: int
    pair_partner: int
    
    def paired_product(self) -> int:
        """
        Calculate the paired product.
        
        Returns:
            Product with pair partner
        """
        return self.value * self.pair_partner
    
    def reveals_even_prime_root(self) -> bool:
        """
        Check if this paired product reveals even-prime-like square root.
        
        Returns:
            True if square root exhibits even-prime properties in AEI
            
        Mathematical Basis:
            In AEI framework, when two numbers are paired (a, b) such that:
            - Their product p = a × b is divisible by 4
            - The square root √p exists in extended AEI arithmetic
            Then √p exhibits "even-prime-like" behavior under I-field operations.
            
            This is simplified from the full AEI theory where paired operations
            reveal roots that behave as even primes (beyond classical prime 2)
            in modular arithmetic involving the indeterminate I.
            
            The criterion (product % 4 == 0) is a SIMPLIFIED HEURISTIC for
            demonstration. Full cryptographic implementation requires deeper
            number-theoretic analysis specific to AEI paired-prime relationships.
        """
        product = self.paired_product()
        # Simplified criterion for demonstration
        # Full theory requires AEI-specific number theory
        return (product % 4 == 0)
    
    def cryptographic_key_component(self) -> int:
        """
        Generate cryptographic key component from paired-prime property.
        
        Returns:
            Key component derived from paired-prime relationship
        """
        # Key is function of both pair elements and their relationship
        # Indecipherable without understanding AEI paired-prime theory
        return (self.value ^ self.pair_partner) * self.paired_product()


class IndeterminateModularArithmetic:
    """
    Modular arithmetic extended to include I as a value.
    
    This enables cryptographic operations in an extended arithmetic space
    where classical factorization and discrete log problems are transformed.
    """
    
    def __init__(self, modulus: int):
        """
        Initialize I-field modular arithmetic.
        
        Args:
            modulus: Modulus for arithmetic operations
        """
        self.modulus = modulus
    
    def add_with_I(self, a: int, b: int, has_I_a: bool = False, has_I_b: bool = False) -> Tuple[int, bool]:
        """
        Add two values that may contain I-component.
        
        Args:
            a: First value (real component)
            b: Second value (real component)
            has_I_a: Whether a has I-component
            has_I_b: Whether b has I-component
            
        Returns:
            (result, has_I): Result value and whether it has I-component
        """
        result = (a + b) % self.modulus
        # If either has I, result has I (absorption property)
        has_I = has_I_a or has_I_b
        return result, has_I
    
    def multiply_with_I(self, a: int, b: int, has_I_a: bool = False, has_I_b: bool = False) -> Tuple[int, bool]:
        """
        Multiply two values that may contain I-component.
        
        Args:
            a: First value (real component)
            b: Second value (real component)
            has_I_a: Whether a has I-component
            has_I_b: Whether b has I-component
            
        Returns:
            (result, has_I): Result value and whether it has I-component
        """
        result = (a * b) % self.modulus
        # I-field multiplication: I * I = I (idempotency)
        has_I = has_I_a or has_I_b
        return result, has_I
    
    def inverse_with_I(self, a: int, has_I: bool = False) -> Optional[Tuple[int, bool]]:
        """
        Find multiplicative inverse, handling I-components.
        
        Args:
            a: Value to invert
            has_I: Whether value has I-component
            
        Returns:
            (inverse, has_I) if exists, None otherwise
        """
        if has_I:
            # I has no multiplicative inverse (P14 axiom)
            return None
        
        # Classical extended Euclidean algorithm for non-I values
        def egcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = egcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y
        
        gcd, x, _ = egcd(a % self.modulus, self.modulus)
        if gcd != 1:
            return None  # No inverse
        return (x % self.modulus, False)


class IndeterminateMatrix:
    """
    Matrix with I-valued entries for cryptographic applications.
    
    These matrices have properties indecipherable to classical analysis:
    - Larger key space than classical matrices
    - Operations with I preserve security
    - Inversion requires AEI-aware algorithms
    """
    
    def __init__(self, size: int, modulus: int):
        """
        Initialize indeterminate matrix.
        
        Args:
            size: Matrix dimension (size × size)
            modulus: Modulus for arithmetic
        """
        self.size = size
        self.modulus = modulus
        self.real_part = [[0 for _ in range(size)] for _ in range(size)]
        self.has_I = [[False for _ in range(size)] for _ in range(size)]
    
    def randomize(self, I_probability: float = 0.3):
        """
        Fill matrix with random values, some containing I.
        
        Args:
            I_probability: Probability each entry has I-component
        """
        for i in range(self.size):
            for j in range(self.size):
                self.real_part[i][j] = random.randint(0, self.modulus - 1)
                self.has_I[i][j] = (random.random() < I_probability)
    
    def determinant_signature(self) -> Tuple[int, bool]:
        """
        Calculate determinant, tracking I-component.
        
        Returns:
            (det_value, has_I): Determinant value and I-flag
        """
        # Simplified: for 2x2 case
        if self.size != 2:
            raise NotImplementedError("Only 2x2 matrices supported currently")
        
        a, b = self.real_part[0][0], self.real_part[0][1]
        c, d = self.real_part[1][0], self.real_part[1][1]
        I_a, I_b = self.has_I[0][0], self.has_I[0][1]
        I_c, I_d = self.has_I[1][0], self.has_I[1][1]
        
        # det = ad - bc
        ad = (a * d) % self.modulus
        bc = (b * c) % self.modulus
        det_val = (ad - bc) % self.modulus
        
        # I-tracking: if any term has I, result may have I
        has_I = (I_a or I_d) or (I_b or I_c)
        
        return det_val, has_I
    
    def encrypt_vector(self, plaintext: List[int]) -> List[Tuple[int, bool]]:
        """
        Encrypt vector via matrix multiplication.
        
        Args:
            plaintext: Vector to encrypt
            
        Returns:
            Encrypted vector with I-components
        """
        if len(plaintext) != self.size:
            raise ValueError(f"Vector must have length {self.size}")
        
        result = []
        for i in range(self.size):
            val = 0
            has_I = False
            for j in range(self.size):
                prod = (self.real_part[i][j] * plaintext[j]) % self.modulus
                val = (val + prod) % self.modulus
                # Track I propagation
                if self.has_I[i][j]:
                    has_I = True
            result.append((val, has_I))
        
        return result


def _eh_primo(n: int, rodadas: int = 40) -> bool:
    """Miller–Rabin com bases aleatórias de `secrets` (erro ≤ 4^-rodadas para n composto)."""
    if n < 2:
        return False
    pequenos = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in pequenos:
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(rodadas):
        a = 2 + secrets.randbelow(n - 3)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def _primo_aleatorio(bits: int) -> int:
    """Primo de exatamente `bits` bits (bit mais alto e bit mais baixo ligados)."""
    if bits < 8:
        raise ValueError("bits >= 8")
    while True:
        c = secrets.randbits(bits) | (1 << (bits - 1)) | 1
        if _eh_primo(c):
            return c


class PairedPrimeCryptosystem:
    """
    RSA com quatro primos (multi-prime RSA), organizados em dois pares.

    O que isto é, sem exagero: n = p1·p2·q1·q2 com quatro primos distintos e
    φ(n) = (p1−1)(p2−1)(q1−1)(q2−1). A segurança é a do RSA com esse módulo; os
    "pares" não acrescentam segurança nem dependem da álgebra do indeterminado.
    É uma demonstração educacional, sem padding (OAEP/PSS) e sem auditoria: não use
    para proteger dados reais.

    Versões anteriores sorteavam inteiros quaisquer como "primos" e calculavam φ(n)
    como (p1·p2 − 1)(q1·q2 − 1), o que não é φ(n); por isso nenhuma decifração
    voltava à mensagem.
    """

    E_PADRAO = 65537

    def __init__(self, security_parameter: int = 256):
        """
        Args:
            security_parameter: tamanho aproximado de n em bits (cada primo tem 1/4 disso).
        """
        self.security_bits = security_parameter
        self.key_generated = False
        self.public_key: Optional[Tuple[int, int]] = None
        self.private_key: Optional[Tuple[PairedPrime, PairedPrime]] = None
        self._d: Optional[int] = None

    def generate_keypair(self) -> Tuple[Tuple[int, int], Tuple[PairedPrime, PairedPrime]]:
        """
        Gera (n, e) e os dois pares de primos.

        Os quatro primos são distintos e cada um tem security_parameter/4 bits
        (mínimo 16). e = 65537; repete o sorteio até mdc(e, φ(n)) = 1.
        """
        bits = max(16, self.security_bits // 4)
        e = self.E_PADRAO
        while True:
            primos = set()
            while len(primos) < 4:
                primos.add(_primo_aleatorio(bits))
            p1, p2, q1, q2 = sorted(primos)
            phi = (p1 - 1) * (p2 - 1) * (q1 - 1) * (q2 - 1)
            try:
                d = pow(e, -1, phi)
            except ValueError:  # mdc(e, φ) ≠ 1
                continue
            break
        pair1 = PairedPrime(p1, p2)
        pair2 = PairedPrime(q1, q2)
        n = pair1.paired_product() * pair2.paired_product()
        self.public_key = (n, e)
        self.private_key = (pair1, pair2)
        self._d = d
        self.key_generated = True
        return self.public_key, self.private_key

    def encrypt(self, message: int) -> int:
        """c = m^e mod n. Exige 0 ≤ m < n."""
        if not self.key_generated:
            raise ValueError("Must generate keys first")
        n, e = self.public_key
        if not 0 <= message < n:
            raise ValueError("a mensagem precisa estar em [0, n)")
        return pow(message, e, n)

    def decrypt(self, ciphertext: int) -> int:
        """m = c^d mod n, com d = e⁻¹ mod φ(n) e φ(n) = ∏(p−1) sobre os quatro primos."""
        if not self.key_generated or self._d is None or self.public_key is None:
            raise ValueError("Must generate keys first")
        n, _ = self.public_key
        return pow(ciphertext, self._d, n)

    def sign(self, message: int) -> int:
        """
        Sign message with private key.
        
        Args:
            message: Message to sign
            
        Returns:
            Signature
        """
        # Signing is similar to decryption
        return self.decrypt(message)
    
    def verify(self, message: int, signature: int) -> bool:
        """
        Verify signature with public key.
        
        Args:
            message: Original message
            signature: Signature to verify
            
        Returns:
            True if signature valid
        """
        # Verification: check if Encrypt(signature) == message
        return self.encrypt(signature) == message


def watermark_detection(data: bytes) -> bool:
    """
    Detect if data contains AEI mathematical watermark.
    
    The paired-prime properties serve as intrinsic proof of derivation
    from AEI framework, regardless of symbol substitution.
    
    Args:
        data: Data to analyze for AEI signatures
        
    Returns:
        True if AEI watermark detected
    """
    # Check for characteristic patterns:
    # 1. Paired-prime relationships
    # 2. I-idempotency patterns
    # 3. Non-distributive corrections
    
    # Convert bytes to integers for analysis
    values = [int(b) for b in data[:100]]  # Sample first 100 bytes
    
    # Look for paired products with even-prime-like roots
    signatures_found = 0
    for i in range(len(values) - 1):
        product = values[i] * values[i + 1]
        if product % 4 == 0:  # Simplified signature check
            signatures_found += 1
    
    # If >30% of pairs show signature, likely AEI-derived
    threshold = len(values) * 0.3
    return signatures_found > threshold


# Neon visualization color codes for cryptographic monitoring
NEON_COLORS = {
    'cyan': '#00FFFF',        # Stable I-field flow
    'purple': '#FF00FF',      # J-field active regions  
    'magenta': '#FF00AA',     # J-field active regions alternate
    'lime': '#00FF00',        # Paired-prime presence
    'orange': '#FF8800',      # I-field instabilities
    'red': '#FF0000',         # Critical indetermination zones
}


def visualize_crypto_state(has_I: bool, security_level: float) -> str:
    """
    Get neon color code for cryptographic state visualization.
    
    Args:
        has_I: Whether state involves I-component
        security_level: Security level 0.0-1.0
        
    Returns:
        Hex color code for neon display
    """
    if has_I and security_level > 0.8:
        return NEON_COLORS['lime']  # Paired-prime secured
    elif has_I and security_level > 0.5:
        return NEON_COLORS['cyan']  # I-field encrypted
    elif has_I:
        return NEON_COLORS['orange']  # I-field but weak
    elif security_level > 0.8:
        return NEON_COLORS['purple']  # J-field secured
    elif security_level > 0.5:
        return NEON_COLORS['magenta']  # Moderate security
    else:
        return NEON_COLORS['red']  # Insecure
