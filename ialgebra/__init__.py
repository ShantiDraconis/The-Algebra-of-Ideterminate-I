"""
The Algebra of Extended Indeterminate (AEI)

A computational algebra system for the indeterminate element I with:
- Flexible resolution framework
- Physics applications (dark sector, modified gravity)
- Cryptographic systems (paired-prime, I-matrix)
- Hardware specifications (Floating-I arithmetic)

Author: Tiago Fagliari (ORCID: 0009-0006-6874-3910)
"""

from .types import (
    ElementType,
    FieldElement,
    Indeterminate,
    ExtendedElement,
    I,
    AlgebraElement,
    to_extended,
    is_indeterminate_element
)

from .operations import (
    add,
    subtract,
    multiply,
    divide,
    power,
    negate,
    add_I,
    multiply_I,
    is_zero,
    equals,
    omega_identity,
    omega_scaled,
    omega_nilpotent
)

from .flexible_resolution import (
    ResolutionStrategy,
    ResolutionContext,
    FlexibleIndeterminateSystem,
    create_system,
    resolve_locally,
    check_collapse
)

from .physics import (
    JField,
    IFieldTensor,
    InflatonIField,
    SmoothSingularity,
    EntropyAcceleration,
    modified_einstein_equation,
    PLANCK_LENGTH,
    PLANCK_TIME,
    PLANCK_MASS,
    PLANCK_ENERGY,
    I_FIELD_SCALE,
    J_FIELD_SCALE
)

from .cryptography import (
    PairedPrime,
    IndeterminateModularArithmetic,
    IndeterminateMatrix,
    PairedPrimeCryptosystem,
    watermark_detection,
    NEON_COLORS,
    visualize_crypto_state
)

__version__ = "0.2.0"
__author__ = "Tiago Fagliari"
__orcid__ = "0009-0006-6874-3910"
__license__ = "See LICENSE file"

__all__ = [
    # Types
    "ElementType",
    "FieldElement",
    "Indeterminate",
    "ExtendedElement",
    "I",
    "AlgebraElement",
    "to_extended",
    "is_indeterminate_element",
    # Operations
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "negate",
    "add_I",
    "multiply_I",
    "is_zero",
    "equals",
    "omega_identity",
    "omega_scaled",
    "omega_nilpotent",
    # Flexible Resolution
    "ResolutionStrategy",
    "ResolutionContext",
    "FlexibleIndeterminateSystem",
    "create_system",
    "resolve_locally",
    "check_collapse",
    # Physics
    "JField",
    "IFieldTensor",
    "InflatonIField",
    "SmoothSingularity",
    "EntropyAcceleration",
    "modified_einstein_equation",
    "PLANCK_LENGTH",
    "PLANCK_TIME",
    "PLANCK_MASS",
    "PLANCK_ENERGY",
    "I_FIELD_SCALE",
    "J_FIELD_SCALE",
    # Cryptography
    "PairedPrime",
    "IndeterminateModularArithmetic",
    "IndeterminateMatrix",
    "PairedPrimeCryptosystem",
    "watermark_detection",
    "NEON_COLORS",
    "visualize_crypto_state",
]
