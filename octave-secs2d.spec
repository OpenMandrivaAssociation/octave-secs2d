%global octpkg secs2d

Summary:	A Drift-Diffusion simulator for 2d semiconductor devices with Octave
Name:		octave-secs2d
Version:	0.0.8
Release:	2
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/secs2d/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/?44803
Patch0:		%{name}-0.0.8-port-to-octave-4.2.1.patch
# https://savannah.gnu.org/bugs/index.php?59606
Patch1:		build-against-octave-6.patch
# https://savannah.gnu.org/bugs/?55345
Patch2:		do-not-strip-debugging-symbols.patch

BuildRequires:  octave-devel >= 2.9.17
#BuildRequires:	dx
#BuildRequires:	gmsh

Requires:	octave(api) = %{octave_api}
#Requires:	dx
#Requires:	gmsh

Requires(post): octave
Requires(postun): octave

%description
A Drift-Diffusion simulator for 2d semiconductor devices with Octave.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

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

