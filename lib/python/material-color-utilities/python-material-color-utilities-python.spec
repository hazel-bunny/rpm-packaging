%global short_name material-color-utilities
%global pypi_name %{short_name}-python
%global module material_color_utilities_python

Name:           python-%{short_name}
Version:        0.1.5
Release:        %autorelease
Summary:        Python port of material-color-utilities used for Material You colors
License:        Apache-2.0

URL:            https://github.com/avanishsubbiah/%{pypi_name}
Source:         %{pypi_source %{pypi_name}}
Patch0:         0001-Removing-Pillow-version-requirement.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  git

%global _description %{expand:
%{summary}}

%description %_description

%package -n     python3-%{short_name}
Summary:        %{summary}

%description -n python3-%{short_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{module}

%check
%pyproject_check_import %{module}

%files -n python3-%{short_name} -f %{pyproject_files}
%license LICENSE.md

%changelog
%autochangelog
