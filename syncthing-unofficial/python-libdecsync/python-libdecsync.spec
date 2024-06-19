%global module libdecsync
%global _basename %{module}-bindings-python3
%global _libPath %{module}/libs

Name:           python-%{module}
Version:        2.2.1

%global forgeurl https://github.com/39aldo39/%{_basename}
%global tag v%{version}
%global date 20211224
%forgemeta

Release:        2%{?dist}
Summary:        Python3 bindings for %{module}
License:        LGPL-2.0
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  libxcrypt-compat
%ifarch x86_64
BuildRequires:  %{module}-devel
%endif
BuildRequires:  %{module}
Requires:       %{module}

%global _description %{expand:
python3-%{module} is a Python3 wrapper around %{module} for synchronizing using DecSync.}

%description %_description

#------------------------------------------------------------------

%package -n     python3-%{module}
Summary:        %{summary}

%description -n python3-%{module} %_description

%files -n python3-%{module} -f %{pyproject_files}
%{python3_sitelib}/%{_libPath}/%{module}.so

#------------------------------------------------------------------

%prep
%forgeautosetup -p1
find %{_libPath} -delete
cat "%{module}/__init__.py" | tr $'\n' $'\r' | sed 's#os_name = platform.system().*not supported")#libpath = resource_filename(__name__, "libs/%{module}.so")#' | tr $'\r' $'\n' > __init__.py.new
mv __init__.py.new %{module}/__init__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{module}
mkdir -p %{buildroot}%{python3_sitelib}/%{_libPath}
ln -s %{_libdir}/%{module}.so %{buildroot}%{python3_sitelib}/%{_libPath}/%{module}.so
# not necessary for every package, but for those who it is, it'd generate conflict with others otherwise
rm -rf %{buildroot}%{python3_sitelib}/tests/

%changelog
%autochangelog
