%global _basename anoise
%global _suffix 3
%global wheel_name %{_basename}_community_extension%{_suffix}

Name:           %{_basename}-community-extension%{_suffix}
Version:        0.0.1
Release:        %autorelease
Summary:        Ambient Noise Community Extension %{_suffix}
License:        GPLv3
URL:            https://costales.github.io/projects/anoise
Source:         https://launchpad.net/~costales/+archive/ubuntu/anoise/+sourcefiles/%{name}/%{version}/%{name}_%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-installer
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

Requires:       anoise-media

Enhances:       anoise

%description
Ambient Noise Community Extension %{_suffix}. Sounds and icons for Anoise Player from users

%prep
%setup -qn media%{_suffix}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

cp -r %{buildroot}%{python3_sitelib}%{_datadir} %{buildroot}%{_prefix}/
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/
cp -r %{buildroot}%{python3_sitelib}/%{wheel_name}-%{version}.dist-info/COPYING.GPL3 %{buildroot}%{_datadir}/licenses/%{name}/
rm -rf %{buildroot}%{python3_sitelib}%{_prefix}/

%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{_basename}/

%files
%license COPYING.GPL3
%doc README
%{_datadir}/%{_basename}/sounds/brown.{ogg,png}
%{_datadir}/%{_basename}/sounds/brown_ossl.{ogg,png}
%{_datadir}/%{_basename}/sounds/pink.{ogg,png}
%{_datadir}/%{_basename}/sounds/white.{ogg,png}
%{python3_sitelib}/%{wheel_name}-%{version}.dist-info/

%changelog
%autochangelog
