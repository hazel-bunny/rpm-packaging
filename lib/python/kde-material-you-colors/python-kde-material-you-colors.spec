%global pypi_name kde-material-you-colors

Name:           python-%{pypi_name}
Version:        1.8.0
Release:        %autorelease
Summary:        Automatic Material You Colors Generator from your wallpaper for the Plasma Desktop
License:        GPL-3.0

URL:            https://github.com/luisbocanegra/%{pypi_name}
Source:         %{pypi_source %{pypi_name}}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Automatically generate light/dark color themes for KDE (and pywal if installed) from your current wallpaper, using @T-Dynamos Python implementation of Google's Material Color Utilities.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%pyproject_extras_subpkg -n python3-%{pypi_name} cli


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -x cli


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}


%changelog
%autochangelog
