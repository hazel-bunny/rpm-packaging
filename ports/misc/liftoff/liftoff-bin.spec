%global _basename liftoff
%global debug_package %{nil}

Name:       %{_basename}-bin
Version:    0.10.10
Release:    1%{?dist}
License:    GPL-2.0
Summary:    A mobile and desktop lemmy client written in flutter
URL:        https://github.com/%{_basename}-app/%{_basename}
Source0:    %{url}/releases/download/v%{version}/liftoff-v%{version}-%{_arch}-linux.tar.gz
Source1:    %{url}/raw/v%{version}/assets/app_icon.svg
Source2:    %{_basename}.desktop

BuildRequires:    gtk-update-icon-cache
BuildRequires:    desktop-file-utils

ExclusiveArch:    x86_64

Provides:   %{_basename} = %{version}
Conflicts:  %{_basename} = %{version}

%description
%summary

%files
%{_bindir}/%{_basename}
%{_datadir}/applications/%{_basename}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{_basename}.svg
/opt/%{_basename}

%prep
%setup -qn %{_basename}-%{version} -c

%build
#nothing

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}/opt/%{_basename}

install -Dm644 %{SOURCE1} "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{_basename}.svg"
install -Dm644 %{SOURCE2} -t "%{buildroot}%{_datadir}/applications/"

cp -ar --no-preserve=ownership data "%{buildroot}/opt/%{_basename}/data"
cp -ar --no-preserve=ownership lib "%{buildroot}/opt/%{_basename}/lib"
cp -a --no-preserve=ownership Liftoff "%{buildroot}/opt/%{_basename}/Liftoff"

ln -s "/opt/%{_basename}/Liftoff"  %{buildroot}%{_bindir}/%{_basename}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{_basename}.desktop

%changelog
* Tue Jun 18 2024 Dipta Biswas <dabiswas112@gmail.com> - 0.10.10-1
- initial package
