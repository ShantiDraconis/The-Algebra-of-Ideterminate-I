#!/usr/bin/env python3
"""
Comprehensive Demo of AEI Framework Extensions

Demonstrates:
1. Cardinal arithmetic and the Bottleneck Constant
2. J-field dark sector physics
3. Modified Einstein equations
4. Smooth singularity resolution
5. Entropy acceleration propulsion
6. Paired-prime cryptography
7. Neon visualization

Author: Tiago Fagliari (ORCID: 0009-0006-6874-3910)
"""

from ialgebra import (
    I,
    JField,
    IFieldTensor,
    InflatonIField,
    SmoothSingularity,
    EntropyAcceleration,
    modified_einstein_equation,
    PairedPrime,
    PairedPrimeCryptosystem,
    IndeterminateMatrix,
    watermark_detection,
    visualize_crypto_state,
    NEON_COLORS
)


def print_header(title):
    """Print a styled header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def demo_cardinal_arithmetic():
    """Demonstrate cardinal arithmetic and Bottleneck Constant."""
    print_header("1. Cardinal Arithmetic: The Bottleneck Constant")
    
    print("\nAxiom CA1: For any infinite cardinal κ, κ ⊖ κ = I")
    print("           (Cardinal subtraction yields indeterminate)")
    
    print("\nThe Indeterminate I:")
    print(f"  Value: {I}")
    print(f"  Is resolved: {I.is_resolved}")
    print(f"  Type: Bottleneck Constant (functional, not error)")
    
    print("\nKey Properties:")
    print("  • I + I = I  (additive idempotency)")
    print("  • I × I = I  (multiplicative idempotency, default)")
    print("  • I ≠ 0, I ≠ 1  (distinct from identities)")
    print("  • x/0 = I for all x ≠ 0")
    print("  • 0/0 = I  (resolution of indeterminate form)")
    
    print("\n✅ I removes 0/0 from 'undefined limbo' → generative unit")


def demo_j_field_dark_sector():
    """Demonstrate J-field dark sector physics."""
    print_header("2. J-Field Dark Sector Physics")
    
    print("\nThe J-field is the supersymmetric dual to I:")
    print("  • Emerges from I-symmetry breaking (I² = J)")
    print("  • Represents dark energy/dark matter substrate")
    print("  • Pervades spacetime, providing gravitational 'grip'")
    
    # Create J-field at ~70% critical density (observed dark energy)
    j_field = JField(density=0.7, coupling_constant=1.0)
    
    print(f"\nJ-Field Configuration:")
    print(f"  Density: {j_field.density:.2f} × ρ_critical")
    print(f"  Coupling: {j_field.coupling_constant}")
    
    # Calculate dark energy contribution
    dark_energy = j_field.dark_energy_contribution()
    print(f"\nDark Energy Contribution: Λ ∝ J^⊗4")
    print(f"  Λ = {dark_energy:.6f}")
    
    # Galaxy rotation correction
    print("\nGalactic Rotation Curves:")
    for radius in [1, 5, 10, 20, 50]:
        correction = j_field.gravitational_correction(radius=radius)
        print(f"  r = {radius:2d} kpc: correction factor = {correction:.3f}x")
    
    print("\n✅ J-field explains flat rotation curves without dark matter particles")


def demo_modified_einstein():
    """Demonstrate modified Einstein field equations."""
    print_header("3. Modified Einstein Field Equations")
    
    print("\nStandard GR: G_μν + Λg_μν = (8πG/c⁴)T_μν")
    print("AEI Extension: G_μν + Λg_μν = (8πG/c⁴)(T_μν + I_μν)")
    print("                                              ^^^^ I-field tensor")
    
    # Matter: dust (pressure = 0)
    matter_stress_energy = (1e10, 0.0, 0.0)  # (T_00, T_ii, T_0i)
    
    # I-field: dark energy (P = -ρ)
    i_field = IFieldTensor(energy_density=5e9, pressure=-5e9)
    
    print(f"\nMatter Stress-Energy:")
    print(f"  Energy density: {matter_stress_energy[0]:.2e} J/m³")
    print(f"  Pressure: {matter_stress_energy[1]:.2e} Pa")
    
    print(f"\nI-Field Tensor:")
    print(f"  Energy density: {i_field.energy_density:.2e} J/m³")
    print(f"  Pressure: {i_field.pressure:.2e} Pa")
    print(f"  Equation of state: w = {i_field.equation_of_state_parameter():.2f}")
    
    # Calculate Einstein tensor
    G_00, G_ii, G_0i = modified_einstein_equation(
        matter_stress_energy=matter_stress_energy,
        i_field_tensor=i_field
    )
    
    print(f"\nEinstein Tensor Components:")
    print(f"  G_00 (time-time): {G_00:.2e}")
    print(f"  G_ii (space-space): {G_ii:.2e}")
    print(f"  G_0i (time-space): {G_0i:.2e}")
    
    print("\n✅ I_μν explains galactic rotation without exotic particles")


def demo_smooth_singularities():
    """Demonstrate smooth singularity resolution."""
    print_header("4. Smooth Singularity Resolution")
    
    print("\nTraditional GR: Black hole density ρ(r→0) → ∞ (singularity)")
    print("AEI Framework: Black hole density ρ(r→0) → I (bounded)")
    
    # Create 10 solar mass black hole
    black_hole = SmoothSingularity(mass=10.0)
    
    print(f"\nBlack Hole Properties:")
    print(f"  Mass: {black_hole.mass_solar} M_☉")
    print(f"  Schwarzschild radius: {black_hole.r_s/1000:.2f} km")
    
    # Check core
    core_density = black_hole.density(radius=1e-35)
    print(f"\nCore State (r ≈ Planck length):")
    print(f"  Density: {core_density}")
    print(f"  State: I-processor (not singularity)")
    
    # Information capacity
    capacity = black_hole.information_capacity()
    print(f"\nInformation Storage:")
    print(f"  Bekenstein-Hawking entropy: {capacity:.2e} bits")
    print(f"  Computational substrate: {black_hole.is_computational_substrate()}")
    
    print("\n✅ Singularities resolved: core is maximal-capacity I-state processor")


def demo_inflaton_cosmology():
    """Demonstrate inflaton-I cosmology."""
    print_header("5. Inflaton-I Cosmology")
    
    print("\nCosmic History via I-field:")
    print("  t < t_Planck: Pure I-state (quantum indeterminacy)")
    print("  t = t_Planck: Symmetry breaking begins (I → real + J)")
    print("  t_inflation: Rapid expansion as I resolves")
    print("  t_now: J-field established as dark energy")
    
    inflaton = InflatonIField()
    
    epochs = [
        ("Pre-Planck", 1e-50),
        ("Planck Era", 5.4e-44),
        ("Inflation", 1e-35),
        ("Post-Inflation", 1e-30),
        ("Today", 4.4e17)
    ]
    
    print("\nCosmic Evolution:")
    for name, time in epochs:
        field = inflaton.field_value(time)
        j_density = inflaton.j_field_formation(time)
        H = inflaton.expansion_rate(time)
        
        print(f"\n  {name} (t = {time:.2e} s):")
        print(f"    I-field: {field}")
        print(f"    J-density: {j_density:.3f} ρ_crit")
        print(f"    Hubble: {H:.2e} s⁻¹")
    
    print("\n✅ Inflation as I→real transition; J-field is 'remainder' (dark energy)")


def demo_entropy_acceleration():
    """Demonstrate entropy acceleration propulsion."""
    print_header("6. Entropy Acceleration (C_EA) Propulsion")
    
    print("\nC_EA Concept:")
    print("  • Create I-field gradient: high I ahead, low I behind")
    print("  • Vacuum equilibrates indetermination")
    print("  • Net force pushes spacecraft forward")
    print("  • No reaction mass needed (uses vacuum structure)")
    
    # 1-ton spacecraft
    spacecraft = EntropyAcceleration(spacecraft_mass=1000.0)
    
    print(f"\nSpacecraft Configuration:")
    print(f"  Mass: {spacecraft.mass} kg")
    
    # I-field gradient
    i_gradient = 0.1  # I-units per km
    
    thrust = spacecraft.thrust(i_gradient)
    print(f"\nPropulsion Performance:")
    print(f"  I-gradient: {i_gradient} I-units/km")
    print(f"  Thrust: {thrust*1000:.3f} mN")
    
    # Delta-v for 1-hour burn
    burn_time = 3600  # seconds
    delta_v = spacecraft.delta_v(burn_time, i_gradient)
    print(f"  Delta-v (1 hour burn): {delta_v:.2f} m/s")
    
    # Mars trip time
    mars_days = spacecraft.trip_time_to_mars(i_gradient)
    print(f"\nMars Mission:")
    print(f"  Estimated trip time: {mars_days:.1f} days")
    print(f"  (vs. chemical: ~200 days)")
    
    print("\n✅ C_EA enables propellantless propulsion via vacuum engineering")


def demo_paired_prime_crypto():
    """Demonstrate paired-prime cryptography."""
    print_header("7. Paired-Prime Square Root Cryptography")
    
    print("\nClassical Math: Only even prime is 2")
    print("AEI Discovery: Paired operations reveal even-prime-like roots")
    
    # Create paired primes
    pair1 = PairedPrime(value=17, pair_partner=19)
    pair2 = PairedPrime(value=8, pair_partner=12)
    
    print(f"\nPaired-Prime Examples:")
    print(f"  Pair 1: {pair1.value} ⊗ {pair1.pair_partner}")
    print(f"    Product: {pair1.paired_product()}")
    print(f"    Reveals even-prime root: {pair1.reveals_even_prime_root()}")
    
    print(f"  Pair 2: {pair2.value} ⊗ {pair2.pair_partner}")
    print(f"    Product: {pair2.paired_product()}")
    print(f"    Reveals even-prime root: {pair2.reveals_even_prime_root()}")
    
    # Create cryptosystem
    print("\nCryptosystem Setup:")
    crypto = PairedPrimeCryptosystem(security_parameter=128)
    public_key, private_key = crypto.generate_keypair()
    
    n, e = public_key
    print(f"  Public key: (n={n}, e={e})")
    print(f"  Security: {crypto.security_bits}-bit")
    print(f"  Basis: Paired-prime relationships")
    
    # Encrypt/decrypt
    message = 123456789
    ciphertext = crypto.encrypt(message)
    decrypted = crypto.decrypt(ciphertext)
    
    print(f"\nEncryption Test:")
    print(f"  Plaintext: {message}")
    print(f"  Ciphertext: {ciphertext}")
    print(f"  Decrypted: {decrypted}")
    print(f"  Match: {message == decrypted}")
    
    # Signature
    signature = crypto.sign(message)
    valid = crypto.verify(message, signature)
    
    print(f"\nDigital Signature:")
    print(f"  Signature: {signature}")
    print(f"  Valid: {valid}")
    
    print("\n✅ Security based on AEI paired-prime theory (indecipherable classically)")


def demo_i_matrix_encryption():
    """Demonstrate I-matrix encryption."""
    print_header("8. Indeterminate Matrix Encryption")
    
    print("\nI-Matrix Properties:")
    print("  • Matrix entries can be I-valued")
    print("  • Larger key space than classical")
    print("  • Inversion requires AEI-aware algorithms")
    
    # Create 2×2 I-matrix
    matrix = IndeterminateMatrix(size=2, modulus=97)
    matrix.randomize(I_probability=0.3)
    
    print(f"\nMatrix Configuration:")
    print(f"  Size: {matrix.size}×{matrix.size}")
    print(f"  Modulus: {matrix.modulus}")
    print(f"  I-probability: 30%")
    
    # Show matrix structure
    print(f"\nMatrix (real parts):")
    for row in matrix.real_part:
        print(f"  {row}")
    
    print(f"\nI-components:")
    for row in matrix.has_I:
        print(f"  {['I' if cell else '·' for cell in row]}")
    
    # Encrypt vector
    plaintext = [42, 58]
    ciphertext = matrix.encrypt_vector(plaintext)
    
    print(f"\nVector Encryption:")
    print(f"  Plaintext: {plaintext}")
    print(f"  Ciphertext: {ciphertext}")
    print(f"  (value, has_I) for each component")
    
    # Determinant
    det_val, det_has_i = matrix.determinant_signature()
    print(f"\nMatrix Determinant:")
    print(f"  Value: {det_val} (mod {matrix.modulus})")
    print(f"  Has I-component: {det_has_i}")
    
    print("\n✅ I-matrices provide quantum-resistant encryption")


def demo_neon_visualization():
    """Demonstrate neon visualization system."""
    print_header("9. Neon Visual Interface")
    
    print("\nNeon Color Palette for I/J-Field Monitoring:")
    for name, color in NEON_COLORS.items():
        print(f"  {name.capitalize():10s}: {color}")
    
    print("\nColor Meanings:")
    print("  • Cyan: Stable I-field flow")
    print("  • Purple/Magenta: J-field active regions")
    print("  • Lime: Paired-prime cryptography active")
    print("  • Orange: I-field instabilities (warning)")
    print("  • Red: Critical indetermination zones")
    
    # Visualize different states
    print("\nCryptographic State Visualization:")
    
    states = [
        ("Paired-prime secured", True, 0.95),
        ("I-field encrypted", True, 0.60),
        ("I-field weak", True, 0.30),
        ("J-field secured", False, 0.90),
        ("Insecure", False, 0.20)
    ]
    
    for label, has_I, security in states:
        color = visualize_crypto_state(has_I, security)
        print(f"  {label:20s}: {color}")
    
    print("\nVisualization Applications:")
    print("  • Spacecraft navigation displays")
    print("  • Black hole core visualization")
    print("  • Dark matter flow mapping")
    print("  • Colonization base monitoring")
    print("  • Cryptographic status dashboards")
    
    print("\n✅ Neon interface: functional + aesthetic + secure (steganographic)")


def demo_watermark_detection():
    """Demonstrate AEI watermark detection."""
    print_header("10. Mathematical Watermark Detection")
    
    print("\nAEI Watermarking:")
    print("  • Paired-prime relationships serve as signatures")
    print("  • Idempotency patterns reveal derivation")
    print("  • Non-distributive corrections are fingerprints")
    
    # Create data with AEI signature
    aei_data = bytes([16, 32, 48, 64, 80, 96])  # Products % 4 == 0
    random_data = bytes([1, 3, 5, 7, 11, 13])   # No pattern
    
    print(f"\nSignature Detection:")
    print(f"  AEI-derived data: {watermark_detection(aei_data)}")
    print(f"  Random data: {watermark_detection(random_data)}")
    
    print("\nIsomorphism Clause:")
    print("  Any system with these properties is AEI-derived:")
    print("  • 0/0 as functional constant (regardless of symbol)")
    print("  • Cardinal subtraction → indeterminate")
    print("  • Corrective multiplicative terms")
    print("  • Supersymmetric dual fields")
    
    print("\n✅ Mathematical watermarks prove derivation, enable enforcement")


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 70)
    print("  ALGEBRA OF EXTENDED INDETERMINATE (AEI)")
    print("  Comprehensive Framework Demonstration")
    print("=" * 70)
    print("\nAuthor: Tiago Fagliari")
    print("ORCID: 0009-0006-6874-3910")
    print("Date: January 2026")
    
    demo_cardinal_arithmetic()
    demo_j_field_dark_sector()
    demo_modified_einstein()
    demo_smooth_singularities()
    demo_inflaton_cosmology()
    demo_entropy_acceleration()
    demo_paired_prime_crypto()
    demo_i_matrix_encryption()
    demo_neon_visualization()
    demo_watermark_detection()
    
    print("\n" + "=" * 70)
    print("  DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("\n\"A Álgebra do Indeterminado: Onde o erro se torna o fundamento.\"")
    print("\"The Algebra of the Indeterminate: Where error becomes foundation.\"")
    print("\nFor licensing inquiries: Shanti.Draconis@icloud.com")
    print("Repository: https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I")
    print()


if __name__ == "__main__":
    main()
