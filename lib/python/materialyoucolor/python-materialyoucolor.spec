%global pypi_name materialyoucolor

Name:           python-%{pypi_name}
Version:        2.0.8
Release:        %autorelease
Summary:        Material You color generation algorithms in python
License:        MIT

URL:            https://github.com/T-Dynamos/%{pypi_name}-python
Source:         %{pypi_source %{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  gcc

%global _description %{expand:
%{summary}}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{pypi_name}


%check
%pyproject_check_import %{pypi_name}


%files -n python3-%{pypi_name} -f %{pyproject_files}


%changelog
%autochangelog
