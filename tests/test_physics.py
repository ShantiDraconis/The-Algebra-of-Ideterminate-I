"""
Tests for AEI Physics Module

Tests the physical applications of the indeterminate algebra:
- J-field dark energy calculations
- Modified Einstein equations
- Inflaton-I cosmology
- Smooth singularity resolution
- Entropy acceleration propulsion
"""

import pytest
import math
from ialgebra.physics import (
    JField,
    IFieldTensor,
    InflatonIField,
    SmoothSingularity,
    EntropyAcceleration,
    modified_einstein_equation,
    PLANCK_LENGTH,
    PLANCK_TIME
)
from ialgebra.types import I, Indeterminate


class TestJField:
    """Test J-field dark sector physics."""
    
    def test_j_field_creation(self):
        """Test creating J-field with density."""
        j = JField(density=0.7, coupling_constant=1.0)
        assert j.density == 0.7
        assert j.coupling_constant == 1.0
    
    def test_dark_energy_contribution(self):
        """Test dark energy from J-field."""
        j = JField(density=0.7)
        dark_energy = j.dark_energy_contribution()
        # Should be proportional to J^4
        expected = 0.7 ** 4
        assert abs(dark_energy - expected) < 1e-10
    
    def test_gravitational_correction(self):
        """Test J-field correction to gravity."""
        j = JField(density=0.5)
        
        # At small radii, correction should be near 1
        correction_small = j.gravitational_correction(radius=1.0)
        assert correction_small > 1.0  # J-field adds grip
        
        # At large radii, correction approaches 1
        correction_large = j.gravitational_correction(radius=100.0)
        assert abs(correction_large - 1.0) < 0.1
    
    def test_galaxy_rotation_correction(self):
        """Test that J-field explains flat rotation curves."""
        j = JField(density=0.8)
        
        # At galactic scales (10 kpc), correction should be significant
        correction = j.gravitational_correction(radius=10.0)
        assert correction > 1.5  # Significant extra "grip"


class TestIFieldTensor:
    """Test I-field energy-momentum tensor."""
    
    def test_tensor_creation(self):
        """Test creating I-field tensor."""
        tensor = IFieldTensor(energy_density=1e10, pressure=-1e10)
        assert tensor.energy_density == 1e10
        assert tensor.pressure == -1e10
    
    def test_stress_energy_components(self):
        """Test tensor components."""
        tensor = IFieldTensor(energy_density=1e10, pressure=5e9)
        T_00, T_ii, T_0i = tensor.stress_energy_components()
        
        assert T_00 == 1e10  # Energy density
        assert T_ii == 5e9   # Spatial pressure
        assert T_0i == 0.0   # No momentum flux (isotropic)
    
    def test_equation_of_state(self):
        """Test equation of state parameter w."""
        # Dark energy: w = -1
        dark_energy = IFieldTensor(energy_density=1e10, pressure=-1e10)
        assert abs(dark_energy.equation_of_state_parameter() + 1.0) < 1e-10
        
        # Matter: w = 0
        matter = IFieldTensor(energy_density=1e10, pressure=0.0)
        assert abs(matter.equation_of_state_parameter()) < 1e-10
        
        # Radiation: w = 1/3
        radiation = IFieldTensor(energy_density=1e10, pressure=1e10 / 3)
        assert abs(radiation.equation_of_state_parameter() - 1/3) < 1e-10


class TestInflatonIField:
    """Test inflaton-I cosmology."""
    
    def test_early_universe_pure_i(self):
        """Test that early universe is pure I-state."""
        inflaton = InflatonIField()
        
        # Before Planck time: pure I
        field = inflaton.field_value(time=1e-50)
        assert isinstance(field, Indeterminate)
        assert not field.is_resolved
    
    def test_inflation_epoch(self):
        """Test inflation period."""
        inflaton = InflatonIField()
        
        # During inflation: I partially resolving
        field = inflaton.field_value(time=1e-35)
        assert isinstance(field, Indeterminate)
    
    def test_j_field_formation(self):
        """Test J-field formation from I-resolution."""
        inflaton = InflatonIField()
        
        # Before Planck time: no J-field
        j_early = inflaton.j_field_formation(time=1e-50)
        assert j_early == 0.0
        
        # After inflation: J-field at ~70% (dark energy)
        j_late = inflaton.j_field_formation(time=1.0)
        assert abs(j_late - 0.7) < 0.01
    
    def test_expansion_rate_evolution(self):
        """Test Hubble parameter evolution."""
        inflaton = InflatonIField()
        
        # During inflation: very high H
        H_inflation = inflaton.expansion_rate(time=1e-35)
        assert H_inflation > 1e40  # Huge during inflation
        
        # Today: H ≈ 70 km/s/Mpc ≈ 2.3e-18 s^-1
        H_today = inflaton.expansion_rate(time=4.4e17)  # 13.8 Gyr
        assert abs(H_today - 2.3e-18) < 1e-18


class TestSmoothSingularity:
    """Test smooth singularity resolution."""
    
    def test_black_hole_creation(self):
        """Test creating black hole with I-core."""
        bh = SmoothSingularity(mass=10.0)  # 10 solar masses
        assert bh.mass_solar == 10.0
        assert bh.r_s > 0  # Has Schwarzschild radius
    
    def test_core_is_i_state(self):
        """Test that core density is I, not infinity."""
        bh = SmoothSingularity(mass=10.0)
        
        # At core (r → 0): density → I
        core_density = bh.density(radius=1e-36)
        assert isinstance(core_density, Indeterminate)
        # Core is in I-state
        assert core_density == I or not core_density.is_resolved
    
    def test_no_infinity(self):
        """Test that density never reaches infinity."""
        bh = SmoothSingularity(mass=10.0)
        
        # Even at Planck scale, density is I (not ∞)
        planck_density = bh.density(radius=PLANCK_LENGTH)
        assert isinstance(planck_density, Indeterminate)
        # This is the key: prevents singularity pathology
    
    def test_information_capacity(self):
        """Test Bekenstein-Hawking information capacity."""
        bh = SmoothSingularity(mass=10.0)
        
        capacity = bh.information_capacity()
        assert capacity > 0  # Has finite (but huge) capacity
        # Capacity proportional to area
        assert capacity > 1e60  # Many bits!
    
    def test_is_computational_substrate(self):
        """Test that I-core is computational substrate."""
        bh = SmoothSingularity(mass=10.0)
        
        # All black holes with I-cores are computational
        assert bh.is_computational_substrate() is True
    
    def test_larger_mass_larger_capacity(self):
        """Test that capacity scales with mass."""
        bh_small = SmoothSingularity(mass=1.0)
        bh_large = SmoothSingularity(mass=10.0)
        
        assert bh_large.information_capacity() > bh_small.information_capacity()


class TestEntropyAcceleration:
    """Test C_EA propulsion system."""
    
    def test_propulsion_creation(self):
        """Test creating C_EA system."""
        spacecraft = EntropyAcceleration(spacecraft_mass=1000.0)  # 1 ton
        assert spacecraft.mass == 1000.0
    
    def test_thrust_from_i_gradient(self):
        """Test thrust calculation from I-field gradient."""
        spacecraft = EntropyAcceleration(spacecraft_mass=1000.0)
        
        # With I-field gradient, should produce thrust
        thrust = spacecraft.thrust(i_gradient=0.1)
        assert thrust > 0  # Positive thrust
    
    def test_zero_gradient_no_thrust(self):
        """Test that zero gradient produces no thrust."""
        spacecraft = EntropyAcceleration(spacecraft_mass=1000.0)
        
        thrust = spacecraft.thrust(i_gradient=0.0)
        assert thrust == 0.0
    
    def test_delta_v_calculation(self):
        """Test velocity change from burn."""
        spacecraft = EntropyAcceleration(spacecraft_mass=1000.0)
        
        # 1-hour burn with moderate gradient
        dv = spacecraft.delta_v(burn_time=3600.0, i_gradient=0.1)
        assert dv > 0  # Velocity increases
    
    def test_mars_trip_time(self):
        """Test estimated Mars trip time."""
        spacecraft = EntropyAcceleration(spacecraft_mass=1000.0)
        
        # With sustainable gradient
        trip_time = spacecraft.trip_time_to_mars(i_gradient=0.1)
        
        # Should be finite and positive
        assert trip_time > 0
        assert trip_time < float('inf')
        
        # Should be much faster than chemical propulsion (months)
        # but still realistic (not days)
        assert trip_time > 10  # At least 10 days
        assert trip_time < 1000  # Less than 3 years


class TestModifiedEinstein:
    """Test modified Einstein equations with I-field."""
    
    def test_einstein_with_i_field(self):
        """Test Einstein equation calculation."""
        # Matter stress-energy
        matter = (1e10, 0.0, 0.0)  # Dust (no pressure)
        
        # I-field contribution
        i_field = IFieldTensor(energy_density=5e9, pressure=-5e9)
        
        # Calculate Einstein tensor
        G_00, G_ii, G_0i = modified_einstein_equation(
            matter_stress_energy=matter,
            i_field_tensor=i_field
        )
        
        # Einstein tensor should include both contributions
        assert G_00 != 0  # Non-zero time-time component
        assert G_ii != 0  # Non-zero space-space component
    
    def test_cosmological_constant_effect(self):
        """Test that Lambda affects spacetime."""
        matter = (1e10, 0.0, 0.0)
        i_field = IFieldTensor(energy_density=0.0, pressure=0.0)
        
        # With Lambda
        G_with_lambda = modified_einstein_equation(
            matter_stress_energy=matter,
            i_field_tensor=i_field,
            cosmological_constant=1e-52
        )
        
        # Without Lambda
        G_without_lambda = modified_einstein_equation(
            matter_stress_energy=matter,
            i_field_tensor=i_field,
            cosmological_constant=0.0
        )
        
        # Should be different
        assert G_with_lambda != G_without_lambda


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
