%global _basename khipro
%global forgeurl https://github.com/rank-coder/%{_basename}-m17n
%global commit c9a49a44a5514375252bd51ef43a1d3f77026b64
%global date 20240714
%forgemeta

%global debug_package %{nil}

Name:             %{_basename}-m17n
Version:          17
Release:          1%{?dist}
Summary:          An m17n version of %{_basename}
License:          MIT
URL:              %{forgeurl}
Source0:          %{forgesource}

Requires:         (fcitx-m17n if fcitx)
Requires:         (fcitx5-m17n if fcitx5)
Requires:         (ibus-m17n if ibus)
Recommends:       (ibus-typing-booster if ibus)

%description
%summary

%files
%license LICENSE
%doc README.md
%{_datadir}/m17n/bn-%{_basename}-%{version}.mim

%prep
%forgeautosetup -p1

%build
#nothing

%install
mkdir -p %{buildroot}%{_datadir}/m17n
install -Dm 644 bn-%{_basename}-%{version}.mim -t %{buildroot}%{_datadir}/m17n/

%changelog
* Wed Jul 17 2024 Hazel Bunny <hazel_bunny@disroot.org> - 17-1.git
- Initial build
