Name:      amdgpu-opengl-switcher
Version:   2.0
Release:   0%{?dist}
License:   GPL
Group:     Unspecified
Summary:   Select needed OpenGL implementation with gl_mesa, gl_zink or gl_pro prefix

URL:       https://github.com/Ashark/archlinux-amdgpu-pro/blob/master/progl

Source0:   %{name}-%{version}.tar.gz

Provides:  amdgpu-opengl-switcher = %{version}-%{release}
Provides:  amdgpu-opengl-switcher(x86-64) = %{version}-%{release}
Requires:  /usr/bin/bash

%description
Select needed opengl implementation with gl_mesa, gl_zink or gl_pro prefix

%files
%{_bindir}/gl_zink
%{_bindir}/gl_pro
%{_bindir}/gl_mesa
%{_datadir}/bash-completion/completions/gl_zink
%{_datadir}/bash-completion/completions/gl_pro
%{_datadir}/bash-completion/completions/gl_mesa

%prep
%autosetup -n %{name}-%{version}

%install
mv usr %{buildroot}/

%changelog
* Wed Jul 19 2023 Dipta Biswas <dabiswas112@gmail.com> - 2.0-0
- Import from gloriouseggroll/nobara copr
