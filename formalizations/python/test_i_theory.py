"""
I-Theory: Test Suite for Physical Equations

This module provides comprehensive tests for the I-theory physical implementations.

Author: I-Theory Research Group
Date: 2026
"""

import unittest
import numpy as np
from i_theory_physics import (
    PhysicalConstants,
    PlanckUnits,
    IParticle,
    Wavefunction,
    Cosmology,
    DarkMatterHalo,
    UltraColdAtoms
)


class TestPhysicalConstants(unittest.TestCase):
    """Test physical constants are correctly defined."""
    
    def test_speed_of_light(self):
        """Test speed of light value."""
        self.assertEqual(PhysicalConstants.c, 299792458.0)
    
    def test_gravitational_constant(self):
        """Test gravitational constant."""
        self.assertAlmostEqual(PhysicalConstants.G, 6.67430e-11, places=15)
    
    def test_planck_constant(self):
        """Test Planck constant relation."""
        expected_h = 2 * np.pi * PhysicalConstants.hbar
        self.assertAlmostEqual(PhysicalConstants.h, expected_h, places=40)
    
    def test_fine_structure_constant(self):
        """Test fine structure constant."""
        self.assertAlmostEqual(PhysicalConstants.alpha, 1.0/137.036, places=6)


class TestPlanckUnits(unittest.TestCase):
    """Test Planck unit calculations."""
    
    def setUp(self):
        self.planck = PlanckUnits()
    
    def test_planck_length_positive(self):
        """Planck length must be positive."""
        self.assertGreater(self.planck.length, 0)
    
    def test_planck_time_positive(self):
        """Planck time must be positive."""
        self.assertGreater(self.planck.time, 0)
    
    def test_planck_mass_positive(self):
        """Planck mass must be positive."""
        self.assertGreater(self.planck.mass, 0)
    
    def test_planck_energy_relation(self):
        """Test E = mc² for Planck mass."""
        expected_energy = self.planck.mass * PhysicalConstants.c**2
        self.assertAlmostEqual(self.planck.energy, expected_energy, places=30)
    
    def test_i_modified_units(self):
        """Test I-modified Planck units scale correctly."""
        I_coupling = 2.0
        planck_i = PlanckUnits(I_coupling)
        
        # I-modified length should scale with sqrt(I)
        expected_i_length = self.planck.length * np.sqrt(I_coupling)
        self.assertAlmostEqual(planck_i.i_length, expected_i_length, places=40)


class TestIParticle(unittest.TestCase):
    """Test I-particle physics."""
    
    def setUp(self):
        # Create a 100 GeV/c² particle
        self.m_I = 100 * 1.78266192e-27  # kg
        self.particle = IParticle(mass=self.m_I)
    
    def test_mass_energy_relation(self):
        """Test E = mc²."""
        expected_energy = self.m_I * PhysicalConstants.c**2
        self.assertAlmostEqual(self.particle.energy, expected_energy, places=30)
    
    def test_gravitational_force(self):
        """Test gravitational force calculation."""
        M_sun = 1.989e30  # kg
        r_earth = 1.496e11  # m
        
        F = self.particle.gravitational_force(M_sun, r_earth)
        
        # Force should be positive
        self.assertGreater(F, 0)
        
        # Force should decrease with distance
        F_far = self.particle.gravitational_force(M_sun, 2 * r_earth)
        self.assertLess(F_far, F)
    
    def test_gravitational_potential(self):
        """Test gravitational potential energy."""
        M_sun = 1.989e30
        r = 1.496e11
        
        U = self.particle.gravitational_potential(M_sun, r)
        
        # Potential should be negative
        self.assertLess(U, 0)
    
    def test_orbital_velocity(self):
        """Test circular orbital velocity."""
        M_sun = 1.989e30
        r_earth = 1.496e11
        
        v = self.particle.orbital_velocity(M_sun, r_earth)
        
        # Earth's orbital velocity is about 30 km/s
        expected_v = np.sqrt(PhysicalConstants.G * M_sun / r_earth)
        self.assertAlmostEqual(v, expected_v, places=5)
        self.assertAlmostEqual(v / 1000, 29.8, places=1)  # km/s
    
    def test_keplers_third_law(self):
        """Test Kepler's third law: T²/r³ = constant."""
        M_sun = 1.989e30
        r1 = 1.496e11  # Earth
        r2 = 2.279e11  # Mars
        
        T1 = self.particle.orbital_period(M_sun, r1)
        T2 = self.particle.orbital_period(M_sun, r2)
        
        # T²/r³ should be equal
        ratio1 = T1**2 / r1**3
        ratio2 = T2**2 / r2**3
        
        self.assertAlmostEqual(ratio1, ratio2, places=15)


class TestWavefunction(unittest.TestCase):
    """Test wavefunction calculations."""
    
    def setUp(self):
        self.m_I = 100 * 1.78266192e-27
        self.wf = Wavefunction(mass=self.m_I)
    
    def test_dispersion_relations(self):
        """Test relativistic and non-relativistic dispersion."""
        k = 1e10  # 1/m
        
        omega_rel = self.wf.dispersion_relativistic(k)
        omega_nonrel = self.wf.dispersion_nonrelativistic(k)
        
        # Both should be positive
        self.assertGreater(omega_rel, 0)
        self.assertGreater(omega_nonrel, 0)
        
        # Relativistic should be larger
        self.assertGreater(omega_rel, omega_nonrel)
    
    def test_de_broglie_wavelength(self):
        """Test thermal de Broglie wavelength."""
        T = 1e-9  # 1 nK
        lambda_dB = self.wf.de_broglie_wavelength(T)
        
        # Should be positive
        self.assertGreater(lambda_dB, 0)
        
        # Should decrease with temperature
        lambda_dB_hot = self.wf.de_broglie_wavelength(1e-6)
        self.assertLess(lambda_dB_hot, lambda_dB)
    
    def test_probability_density(self):
        """Test probability density calculation."""
        psi = 1.0 + 1.0j
        rho = self.wf.probability_density(psi)
        
        # Should equal |ψ|²
        expected_rho = np.abs(psi)**2
        self.assertAlmostEqual(rho, expected_rho)
        
        # Should be non-negative
        self.assertGreaterEqual(rho, 0)
    
    def test_plane_wave(self):
        """Test plane wave solution."""
        A = 1.0 + 0j
        k = np.array([1e10, 0, 0])
        omega = self.wf.dispersion_relativistic(np.linalg.norm(k))
        
        psi_func = self.wf.plane_wave(A, k, omega)
        
        # Test at origin and t=0
        r = np.array([0.0, 0.0, 0.0])
        t = 0.0
        psi = psi_func(r, t)
        
        # At origin and t=0, should equal A
        self.assertAlmostEqual(np.abs(psi), np.abs(A))


class TestCosmology(unittest.TestCase):
    """Test cosmological calculations."""
    
    def test_redshift_calculation(self):
        """Test redshift formula."""
        lambda_emit = 500e-9  # 500 nm
        lambda_obs = 700e-9   # 700 nm
        
        z = Cosmology.redshift(lambda_emit, lambda_obs)
        
        expected_z = (lambda_obs - lambda_emit) / lambda_emit
        self.assertAlmostEqual(z, expected_z)
        self.assertAlmostEqual(z, 0.4, places=10)
    
    def test_cmb_temperature_scaling(self):
        """Test CMB temperature scales with (1+z)."""
        z = 1.0
        T = Cosmology.cmb_temperature(z)
        
        expected_T = PhysicalConstants.T_CMB_0 * (1 + z)
        self.assertAlmostEqual(T, expected_T)
        self.assertAlmostEqual(T, 2 * PhysicalConstants.T_CMB_0)
    
    def test_scale_factor_ratio(self):
        """Test scale factor ratio."""
        z = 2.0
        ratio = Cosmology.scale_factor_ratio(z)
        
        self.assertEqual(ratio, 1 + z)
        self.assertEqual(ratio, 3.0)
    
    def test_hubble_velocity(self):
        """Test Hubble's law."""
        d = 3.086e22  # 1 Mpc in m
        v = Cosmology.hubble_velocity(d)
        
        # Should be approximately 67.4 km/s for 1 Mpc
        v_kms = v / 1000
        self.assertAlmostEqual(v_kms, 67.4, places=1)


class TestDarkMatterHalo(unittest.TestCase):
    """Test dark matter halo calculations."""
    
    def test_nfw_profile(self):
        """Test NFW density profile."""
        rho_0 = 1e-21  # kg/m³
        r_s = 20e3 * 3.086e16  # 20 kpc
        
        # At r = r_s, density should be rho_0/4
        rho_rs = DarkMatterHalo.nfw_profile(rho_0, r_s, r_s)
        expected_rho = rho_0 / 4
        self.assertAlmostEqual(rho_rs, expected_rho, places=25)
        
        # Density should decrease with radius
        rho_2rs = DarkMatterHalo.nfw_profile(rho_0, r_s, 2*r_s)
        self.assertLess(rho_2rs, rho_rs)
    
    def test_enclosed_mass(self):
        """Test enclosed mass calculation."""
        rho_0 = 1e-21
        r_s = 20e3 * 3.086e16
        R = r_s
        
        M = DarkMatterHalo.enclosed_mass_nfw(rho_0, r_s, R)
        
        # Mass should be positive
        self.assertGreater(M, 0)
        
        # Mass should increase with radius
        M_larger = DarkMatterHalo.enclosed_mass_nfw(rho_0, r_s, 2*R)
        self.assertGreater(M_larger, M)
    
    def test_jeans_mass(self):
        """Test Jeans mass calculation."""
        T = 1e4  # K
        m = 1.67e-27  # proton mass, kg
        rho = 1e-21  # kg/m³
        
        M_J = DarkMatterHalo.jeans_mass(T, m, rho)
        
        # Jeans mass should be positive
        self.assertGreater(M_J, 0)
        
        # Should increase with temperature
        M_J_hot = DarkMatterHalo.jeans_mass(2*T, m, rho)
        self.assertGreater(M_J_hot, M_J)


class TestUltraColdAtoms(unittest.TestCase):
    """Test ultra-cold atom physics."""
    
    def test_photon_energy(self):
        """Test photon energy calculation."""
        lambda_red = PhysicalConstants.lambda_Li_D1
        E = UltraColdAtoms.photon_energy(lambda_red)
        
        # Energy should be positive
        self.assertGreater(E, 0)
        
        # Energy should be inversely proportional to wavelength
        E_blue = UltraColdAtoms.photon_energy(lambda_red / 2)
        self.assertAlmostEqual(E_blue, 2 * E, places=30)
    
    def test_thermal_energy(self):
        """Test thermal energy."""
        T = 300  # K (room temperature)
        E_thermal = UltraColdAtoms.thermal_energy(T)
        
        # Should be approximately 38 meV at room temp
        E_eV = E_thermal / 1.602e-19
        self.assertAlmostEqual(E_eV, 0.0388, places=3)
    
    def test_bec_critical_temperature(self):
        """Test BEC critical temperature."""
        m_Li = 7 * 1.66054e-27  # Lithium-7 mass
        n = 1e14  # particles per m³
        
        T_c = UltraColdAtoms.bec_critical_temperature(m_Li, n)
        
        # Critical temperature should be positive
        self.assertGreater(T_c, 0)
        
        # Should increase with density
        T_c_dense = UltraColdAtoms.bec_critical_temperature(m_Li, 10*n)
        self.assertGreater(T_c_dense, T_c)


class TestIntegration(unittest.TestCase):
    """Integration tests combining multiple components."""
    
    def test_quantum_gravity_scales(self):
        """Test that quantum and gravitational scales meet at Planck scale."""
        planck = PlanckUnits()
        
        # At Planck scale, Schwarzschild radius ~ Compton wavelength (within factor of 2)
        r_S = 2 * PhysicalConstants.G * planck.mass / PhysicalConstants.c**2
        lambda_C = PhysicalConstants.hbar / (planck.mass * PhysicalConstants.c)
        
        # They should be within the same order of magnitude
        self.assertAlmostEqual(r_S / lambda_C, 2.0, places=10)
    
    def test_cosmology_lithium_analogy(self):
        """Test scale correspondence between atomic and cosmological physics."""
        # Lithium BEC temperature ratio
        T_bec = 1e-9  # K
        T_room = 300  # K
        ratio_atomic = T_bec / T_room
        
        # Cosmological temperature ratio
        planck = PlanckUnits()
        T_cmb = PhysicalConstants.T_CMB_0
        ratio_cosmic = T_cmb / planck.temperature
        
        # Both should be extremely small (order 10^-9 to 10^-32)
        self.assertLess(ratio_atomic, 1e-8)
        self.assertLess(ratio_cosmic, 1e-30)


def run_tests():
    """Run all tests and display results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestPhysicalConstants))
    suite.addTests(loader.loadTestsFromTestCase(TestPlanckUnits))
    suite.addTests(loader.loadTestsFromTestCase(TestIParticle))
    suite.addTests(loader.loadTestsFromTestCase(TestWavefunction))
    suite.addTests(loader.loadTestsFromTestCase(TestCosmology))
    suite.addTests(loader.loadTestsFromTestCase(TestDarkMatterHalo))
    suite.addTests(loader.loadTestsFromTestCase(TestUltraColdAtoms))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
