Name:      amdgpu-opencl-switcher
Version:   1.1
Release:   0%{?dist}
License:   GPL
Group:     Unspecified
Summary:   Select needed OpenCL implementation with cl_pro prefix

Source0:   %{name}-%{version}.tar.gz

URL:       https://github.com/CosmicFusion/amdgpu-opencl-switcher

Provides:  amdgpu-opencl-switcher = %{version}-%{release}
Provides:  amdgpu-opencl-switcher(x86-64) = %{version}-%{release}
Requires:  /usr/bin/bash

%description
Select needed opencl implementation with cl_pro prefix

%files
%{_bindir}/cl_pro
%{_datadir}/bash-completion/completions/cl_pro

%prep
%autosetup -n %{name}-%{version}

%install
mv usr %{buildroot}/

%changelog
* Wed Jul 19 2023 Dipta Biswas <dabiswas112@gmail.com> - 1.1-0
- Import from gloriouseggroll/nobara copr
