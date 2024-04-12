%global module pip-system-certs
%global snake_case pip_system_certs

Name:           python-%{module}
Version:        4.0
Release:        %autorelease
Summary:        Live patches pip to use system certs by default
License:        BSD-2-Clause
URL:            https://gitlab.com/alelec/%{module}
Source:         %{pypi_source pip_system_certs}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package patches pip and requests at runtime to use certificates from the default system store (rather than the bundled certs ca). This will allow pip to verify tls/ssl connections to servers who's cert is trusted by your system install.}

%description %_description

%package -n     python3-%{module}
Summary:        %{summary}

%description -n python3-%{module} %_description


%prep
%autosetup -p1 -n %{snake_case}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files %{snake_case}

%check
%pyproject_check_import %{snake_case}

%files -n python3-%{module} -f %{pyproject_files}
%{python3_sitelib}/%{snake_case}.pth

%changelog
%autochangelog
