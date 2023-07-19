Name:          nobara-amdgpu-config
Version:       2.1
Release:       0%{?dist}
License:       GPLv2
Group:         System Environment/Libraries
Summary:       GUI Installer for amdgpu-pro stack in fedora / nobara

URL:           https://github.com/CosmicFusion/nobara-amdgpu-config

Source0:       %{name}-%{version}.tar.gz
Source1:       https://raw.githubusercontent.com/CosmicFusion/nobara-amdgpu-config/main/LICENSE.md

BuildRequires: wget

Requires:      /usr/bin/bash
Requires:      /usr/bin/rpmbuild
Requires:      fedora-packager
Requires:      rpmdevtools
Requires:      mock
Requires:      zenity

%description
GUI Installer for amdgpu-pro stack in fedora / nobara

%files
%{_sysconfdir}/nobara/scripts/amdgpu-build.sh
%{_sysconfdir}/nobara/scripts/amdgpu-modify.sh
%{_sysconfdir}/nobara/scripts/amdgpu-remove.sh
%{_sysconfdir}/nobara/scripts/nobara-amdgpu-config.ui
%{_sysconfdir}/nobara/scripts/nobara-amdgpu-config.py
%{_bindir}/nobara-amdgpu-config
%{_datadir}/licenses/nobara-amdgpu-config/LICENSE

%prep
%autosetup -n %{name}-%{version}

%install
mv usr %{buildroot}/
mv etc %{buildroot}/
mkdir -p %{buildroot}%{datadir}/licenses/nobara-amdgpu-config
mv LICENSE.md %{buildroot}%{datadir}/licenses/nobara-amdgpu-config/LICENSE

%changelog
* Wed Jul 19 2023 Dipta Biswas <dabiswas112@gmail.com> - 2.1-0
- Import from gloriouseggroll/nobara copr
