%define	pkgname secs2d

Summary:	Octave drift-diffusion simulator for 2D devices
Name:       octave-%{pkgname}
Version:	0.0.8
Release:       3
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/secs2d/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 2.9.17
BuildRequires:  octave-devel >= 2.9.17
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)

%description
Octave drift-diffusion simulator for 2D semiconductor devices.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
%__install -m 755 -d %{buildroot}%{_libdir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
export OCT_ARCH_PREFIX=%{buildroot}%{_libdir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX $OCT_ARCH_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}
%{_libdir}/octave/packages/%{pkgname}-%{version}
