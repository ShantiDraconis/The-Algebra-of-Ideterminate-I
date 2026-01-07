"""
I-Theory: Physical Constants and Fundamental Equations

This module implements the fundamental physical equations and constants
from sections 22-28 of the I-theory framework.

Author: I-Theory Research Group
Date: 2026
"""

import numpy as np
from typing import Union, Tuple, Callable
from dataclasses import dataclass


# Physical Constants (SI units)
class PhysicalConstants:
    """Fundamental physical constants in SI units."""
    
    # Speed of light [m/s]
    c = 299792458.0
    
    # Gravitational constant [m³/(kg⋅s²)]
    G = 6.67430e-11
    
    # Reduced Planck constant [J⋅s]
    hbar = 1.054571817e-34
    
    # Planck constant [J⋅s]
    h = 2 * np.pi * hbar
    
    # Boltzmann constant [J/K]
    k_B = 1.380649e-23
    
    # Hubble constant [km/s/Mpc]
    H_0_kmsMpc = 67.4
    
    # Hubble constant [1/s]
    H_0 = H_0_kmsMpc * 1e3 / 3.086e22
    
    # CMB temperature today [K]
    T_CMB_0 = 2.725
    
    # Fine structure constant [dimensionless]
    alpha = 1.0 / 137.036
    
    # Lithium D-line wavelengths [m]
    lambda_Li_D1 = 670.776e-9
    lambda_Li_D2 = 670.791e-9


class PlanckUnits:
    """Planck units derived from fundamental constants."""
    
    def __init__(self, I_coupling: float = 1.0):
        """
        Initialize Planck units with optional I-coupling.
        
        Args:
            I_coupling: The I-field coupling constant (default 1.0)
        """
        self.I_coupling = I_coupling
        
        # Standard Planck units
        self.length = np.sqrt(
            PhysicalConstants.hbar * PhysicalConstants.G / PhysicalConstants.c**3
        )
        self.time = np.sqrt(
            PhysicalConstants.hbar * PhysicalConstants.G / PhysicalConstants.c**5
        )
        self.mass = np.sqrt(
            PhysicalConstants.hbar * PhysicalConstants.c / PhysicalConstants.G
        )
        self.energy = self.mass * PhysicalConstants.c**2
        self.temperature = self.energy / PhysicalConstants.k_B
        
        # I-modified Planck units
        self.i_length = self.length * np.sqrt(I_coupling)
        self.i_time = self.time * np.sqrt(I_coupling)
        self.i_mass = self.mass / np.sqrt(I_coupling)
        self.i_energy = self.i_mass * PhysicalConstants.c**2
        self.i_temperature = self.i_energy / PhysicalConstants.k_B
    
    def __repr__(self) -> str:
        return (
            f"PlanckUnits(I_coupling={self.I_coupling:.3e})\n"
            f"  length: {self.length:.3e} m\n"
            f"  time: {self.time:.3e} s\n"
            f"  mass: {self.mass:.3e} kg\n"
            f"  energy: {self.energy:.3e} J\n"
            f"  temperature: {self.temperature:.3e} K"
        )


@dataclass
class IParticle:
    """Represents an I-particle with mass and properties."""
    
    mass: float  # [kg]
    position: np.ndarray = None  # [m]
    momentum: np.ndarray = None  # [kg⋅m/s]
    
    def __post_init__(self):
        if self.position is None:
            self.position = np.zeros(3)
        if self.momentum is None:
            self.momentum = np.zeros(3)
    
    @property
    def energy(self) -> float:
        """Mass-energy: E = mc²"""
        return self.mass * PhysicalConstants.c**2
    
    @property
    def kinetic_energy(self) -> float:
        """Kinetic energy (non-relativistic): K = p²/(2m)"""
        p_squared = np.sum(self.momentum**2)
        return p_squared / (2 * self.mass)
    
    @property
    def relativistic_energy(self) -> float:
        """Relativistic energy: E = √((pc)² + (mc²)²)"""
        p = np.linalg.norm(self.momentum)
        return np.sqrt((p * PhysicalConstants.c)**2 + self.energy**2)
    
    def gravitational_force(self, M: float, r: float) -> float:
        """
        Gravitational force on I-particle near mass M at distance r.
        
        F = G m_I M / r²
        
        Args:
            M: Central mass [kg]
            r: Distance [m]
        
        Returns:
            Gravitational force magnitude [N]
        """
        if r <= 0:
            raise ValueError("Distance r must be positive")
        return PhysicalConstants.G * self.mass * M / r**2
    
    def gravitational_potential(self, M: float, r: float) -> float:
        """
        Gravitational potential energy: U = -GMm/r
        
        Args:
            M: Central mass [kg]
            r: Distance [m]
        
        Returns:
            Potential energy [J]
        """
        if r <= 0:
            raise ValueError("Distance r must be positive")
        return -PhysicalConstants.G * M * self.mass / r
    
    def orbital_velocity(self, M: float, r: float) -> float:
        """
        Circular orbital velocity: v = √(GM/r)
        
        Args:
            M: Central mass [kg]
            r: Orbital radius [m]
        
        Returns:
            Orbital velocity [m/s]
        """
        if r <= 0:
            raise ValueError("Radius r must be positive")
        return np.sqrt(PhysicalConstants.G * M / r)
    
    def orbital_period(self, M: float, r: float) -> float:
        """
        Orbital period: T = 2π√(r³/GM)
        
        Args:
            M: Central mass [kg]
            r: Orbital radius [m]
        
        Returns:
            Orbital period [s]
        """
        if r <= 0:
            raise ValueError("Radius r must be positive")
        return 2 * np.pi * np.sqrt(r**3 / (PhysicalConstants.G * M))


class Wavefunction:
    """Quantum wavefunction for I-particles."""
    
    def __init__(self, mass: float):
        """
        Initialize wavefunction for particle of given mass.
        
        Args:
            mass: Particle mass [kg]
        """
        self.mass = mass
    
    def plane_wave(
        self, 
        A: complex, 
        k: np.ndarray, 
        omega: float
    ) -> Callable:
        """
        Create plane wave: Ψ(r,t) = A exp(i(k·r - ωt))
        
        Args:
            A: Amplitude
            k: Wave vector [1/m]
            omega: Angular frequency [1/s]
        
        Returns:
            Function Ψ(r, t) -> complex
        """
        def psi(r: np.ndarray, t: float) -> complex:
            k_dot_r = np.dot(k, r)
            phase = k_dot_r - omega * t
            return A * np.exp(1j * phase)
        return psi
    
    def dispersion_relativistic(self, k: float) -> float:
        """
        Relativistic dispersion: ω = √(k²c² + (mc/ℏ)²)
        
        Args:
            k: Wave number [1/m]
        
        Returns:
            Angular frequency [1/s]
        """
        k_norm = np.abs(k)
        return np.sqrt(
            k_norm**2 * PhysicalConstants.c**2 + 
            (self.mass * PhysicalConstants.c / PhysicalConstants.hbar)**2
        )
    
    def dispersion_nonrelativistic(self, k: float) -> float:
        """
        Non-relativistic dispersion: ω = ℏk²/(2m)
        
        Args:
            k: Wave number [1/m]
        
        Returns:
            Angular frequency [1/s]
        """
        k_norm = np.abs(k)
        return PhysicalConstants.hbar * k_norm**2 / (2 * self.mass)
    
    def de_broglie_wavelength(self, T: float) -> float:
        """
        Thermal de Broglie wavelength: λ = h/√(2mkT)
        
        Args:
            T: Temperature [K]
        
        Returns:
            de Broglie wavelength [m]
        """
        if T <= 0:
            raise ValueError("Temperature must be positive")
        return PhysicalConstants.h / np.sqrt(
            2 * self.mass * PhysicalConstants.k_B * T
        )
    
    def probability_density(self, psi: complex) -> float:
        """
        Probability density: ρ = |Ψ|²
        
        Args:
            psi: Wavefunction value
        
        Returns:
            Probability density
        """
        return np.abs(psi)**2
    
    def gravitational_bohr_radius(self, M: float) -> float:
        """
        Gravitational Bohr radius: a_G = ℏ²/(Gm²M)
        
        Args:
            M: Central mass [kg]
        
        Returns:
            Gravitational Bohr radius [m]
        """
        if M <= 0:
            raise ValueError("Mass M must be positive")
        return PhysicalConstants.hbar**2 / (
            PhysicalConstants.G * self.mass**2 * M
        )


class Cosmology:
    """Cosmological calculations and redshift relations."""
    
    @staticmethod
    def redshift(lambda_emit: float, lambda_obs: float) -> float:
        """
        Calculate redshift: z = (λ_obs - λ_emit) / λ_emit
        
        Args:
            lambda_emit: Emitted wavelength [m]
            lambda_obs: Observed wavelength [m]
        
        Returns:
            Redshift parameter z [dimensionless]
        """
        if lambda_emit <= 0:
            raise ValueError("Emitted wavelength must be positive")
        return (lambda_obs - lambda_emit) / lambda_emit
    
    @staticmethod
    def cmb_temperature(z: float) -> float:
        """
        CMB temperature at redshift z: T(z) = T₀(1+z)
        
        Args:
            z: Redshift
        
        Returns:
            CMB temperature [K]
        """
        return PhysicalConstants.T_CMB_0 * (1 + z)
    
    @staticmethod
    def scale_factor_ratio(z: float) -> float:
        """
        Scale factor ratio: 1+z = a₀/a(t)
        
        Args:
            z: Redshift
        
        Returns:
            Scale factor ratio
        """
        return 1 + z
    
    @staticmethod
    def hubble_velocity(d: float) -> float:
        """
        Hubble's law: v = H₀d
        
        Args:
            d: Distance [m]
        
        Returns:
            Recession velocity [m/s]
        """
        return PhysicalConstants.H_0 * d


class DarkMatterHalo:
    """Dark matter halo density profiles and properties."""
    
    @staticmethod
    def nfw_profile(rho_0: float, r_s: float, r: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        """
        NFW density profile: ρ(r) = ρ₀/[(r/r_s)(1 + r/r_s)²]
        
        Args:
            rho_0: Characteristic density [kg/m³]
            r_s: Scale radius [m]
            r: Radius [m]
        
        Returns:
            Density at radius r [kg/m³]
        """
        if r_s <= 0:
            raise ValueError("Scale radius must be positive")
        x = r / r_s
        return rho_0 / (x * (1 + x)**2)
    
    @staticmethod
    def enclosed_mass_nfw(rho_0: float, r_s: float, R: float) -> float:
        """
        Total mass within radius R for NFW profile.
        
        M(R) = 4πρ₀r_s³[ln(1+R/r_s) - (R/r_s)/(1+R/r_s)]
        
        Args:
            rho_0: Characteristic density [kg/m³]
            r_s: Scale radius [m]
            R: Outer radius [m]
        
        Returns:
            Enclosed mass [kg]
        """
        if r_s <= 0 or R <= 0:
            raise ValueError("Radii must be positive")
        x = R / r_s
        return 4 * np.pi * rho_0 * r_s**3 * (
            np.log(1 + x) - x / (1 + x)
        )
    
    @staticmethod
    def jeans_mass(T: float, m: float, rho: float) -> float:
        """
        Jeans mass: M_J = ((5k_BT)/(Gm))^(3/2) √(3/(4πρ))
        
        Args:
            T: Temperature [K]
            m: Particle mass [kg]
            rho: Density [kg/m³]
        
        Returns:
            Jeans mass [kg]
        """
        if T <= 0 or m <= 0 or rho <= 0:
            raise ValueError("All parameters must be positive")
        
        factor1 = (5 * PhysicalConstants.k_B * T) / (PhysicalConstants.G * m)
        factor2 = 3 / (4 * np.pi * rho)
        
        return factor1**(3/2) * np.sqrt(factor2)


class UltraColdAtoms:
    """Ultra-cold atomic systems and BEC."""
    
    @staticmethod
    def photon_energy(lambda_wavelength: float) -> float:
        """
        Photon energy: E = hc/λ
        
        Args:
            lambda_wavelength: Wavelength [m]
        
        Returns:
            Photon energy [J]
        """
        if lambda_wavelength <= 0:
            raise ValueError("Wavelength must be positive")
        return PhysicalConstants.h * PhysicalConstants.c / lambda_wavelength
    
    @staticmethod
    def thermal_energy(T: float) -> float:
        """
        Thermal energy: E = (3/2)k_BT
        
        Args:
            T: Temperature [K]
        
        Returns:
            Thermal energy [J]
        """
        return 1.5 * PhysicalConstants.k_B * T
    
    @staticmethod
    def bec_critical_temperature(m: float, n: float) -> float:
        """
        BEC critical temperature: T_c = (2πℏ²/mk_B)(n/ζ(3/2))^(2/3)
        
        Args:
            m: Particle mass [kg]
            n: Number density [1/m³]
        
        Returns:
            Critical temperature [K]
        """
        if m <= 0 or n <= 0:
            raise ValueError("Mass and density must be positive")
        
        zeta_3_2 = 2.612  # ζ(3/2) Riemann zeta function
        
        return (2 * np.pi * PhysicalConstants.hbar**2 / (m * PhysicalConstants.k_B)) * \
               (n / zeta_3_2)**(2/3)


# Example usage and tests
if __name__ == "__main__":
    print("=" * 70)
    print("I-Theory Physical Constants and Equations")
    print("=" * 70)
    
    # Display Planck units
    print("\n1. Planck Units:")
    planck = PlanckUnits()
    print(planck)
    
    # Create I-particle
    print("\n2. I-Particle Properties:")
    m_I = 100 * 1.78266192e-27  # 100 GeV/c² in kg
    particle = IParticle(mass=m_I)
    print(f"  Mass: {particle.mass:.3e} kg")
    print(f"  Rest energy: {particle.energy:.3e} J ({particle.energy/1.602e-19:.3e} eV)")
    
    # Gravitational interactions
    print("\n3. Gravitational Interactions:")
    M_sun = 1.989e30  # kg
    r_earth = 1.496e11  # m
    F_grav = particle.gravitational_force(M_sun, r_earth)
    v_orbital = particle.orbital_velocity(M_sun, r_earth)
    T_orbital = particle.orbital_period(M_sun, r_earth)
    print(f"  Force on I-particle near Sun: {F_grav:.3e} N")
    print(f"  Orbital velocity at Earth distance: {v_orbital:.3e} m/s")
    print(f"  Orbital period: {T_orbital/(365.25*24*3600):.3f} years")
    
    # Wavefunction properties
    print("\n4. Wavefunction Properties:")
    wf = Wavefunction(mass=m_I)
    k = 1e10  # 1/m
    omega = wf.dispersion_relativistic(k)
    lambda_dB = wf.de_broglie_wavelength(T=1e-9)
    print(f"  Dispersion relation ω(k={k:.3e}): {omega:.3e} rad/s")
    print(f"  de Broglie wavelength at T=1nK: {lambda_dB:.3e} m")
    
    # Cosmology
    print("\n5. Cosmological Redshift:")
    lambda_emit = 500e-9  # 500 nm
    lambda_obs = 700e-9   # 700 nm (redshifted)
    z = Cosmology.redshift(lambda_emit, lambda_obs)
    T_cmb = Cosmology.cmb_temperature(z)
    print(f"  Redshift z: {z:.3f}")
    print(f"  CMB temperature at z={z:.3f}: {T_cmb:.3f} K")
    
    # Dark matter halo
    print("\n6. Dark Matter Halo (NFW Profile):")
    rho_0 = 1e-21  # kg/m³
    r_s = 20e3 * 3.086e16  # 20 kpc in m
    r = 8e3 * 3.086e16  # 8 kpc (solar distance)
    rho_local = DarkMatterHalo.nfw_profile(rho_0, r_s, r)
    M_enclosed = DarkMatterHalo.enclosed_mass_nfw(rho_0, r_s, r)
    print(f"  Local density at r=8kpc: {rho_local:.3e} kg/m³")
    print(f"  Enclosed mass within 8kpc: {M_enclosed/1.989e30:.3e} M_sun")
    
    print("\n" + "=" * 70)
