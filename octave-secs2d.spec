%define octpkg secs2d

Summary:	A Drift-Diffusion simulator for 2d semiconductor devices with Octave
Name:		octave-%{octpkg}
Version:	0.0.8
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/?44803
Patch0:		%{name}-0.0.8-port-to-octave-4.2.1.patch
# https://savannah.gnu.org/bugs/index.php?59606
Patch1:		build-against-octave-6.patch
# https://savannah.gnu.org/bugs/?55345
Patch2:		do-not-strip-debugging-symbols.patch
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 2.9.17

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A Drift-Diffusion simulator for 2d semiconductor devices with Octave.

This package is part of external Octave-Forge collection.

%files
%license COPYING
#doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

