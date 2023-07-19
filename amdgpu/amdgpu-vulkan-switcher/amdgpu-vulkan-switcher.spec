Name:      amdgpu-vulkan-switcher
License:   GPL
Version:   2.0
Release:   5%{?dist}
Summary:   Select needed vulkan implementation with vk_radv, vk_amdvlk or vk_pro prefix

URL:       https://gitlab.com/AndrewShark/amd-vulkan-prefixes

Source0:   %{name}-%{version}.tar.gz

Requires:  amdgpu-opengl-switcher

%description
Select needed vulkan implementation with vk_radv, vk_amdvlk or vk_pro prefix

%files
%{_bindir}/vk_radv
%{_bindir}/vk_amdvlk
%{_bindir}/vk_pro
%{_bindir}/vk_legacy
%{_datadir}/bash-completion/completions/vk_radv
%{_datadir}/bash-completion/completions/vk_amdvlk
%{_datadir}/bash-completion/completions/vk_pro
%{_datadir}/bash-completion/completions/vk_legacy

%prep
%autosetup -n %{name}-%{version}

%install
mv usr %{buildroot}/

%changelog
* Wed Jul 19 2023 Dipta Biswas <dabiswas112@gmail.com> - 2.0-5
- Import from gloriouseggroll/nobara copr
