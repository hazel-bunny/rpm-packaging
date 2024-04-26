%global _libPath libdecsync/libs

Name:           python-libdecsync
Version:        2.2.1
Release:        %autorelease
Summary:        Python3 bindings for libdecsync

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPLv2
URL:            https://github.com/39aldo39/libdecsync-bindings-python3
Source:         %{pypi_source libdecsync}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  libxcrypt-compat
BuildRequires:  libdecsync-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
python3-libdecsync is a Python3 wrapper around libdecsync for synchronizing using DecSync.}


%description %_description

%package -n     python3-libdecsync
Summary:        %{summary}

%description -n python3-libdecsync %_description


%prep
%autosetup -p1 -n libdecsync-%{version}
find %{_libPath} -delete
cat "libdecsync/__init__.py" | tr $'\n' $'\r' | sed 's#os_name = platform.system().*not supported")#libpath = resource_filename(__name__, "libs/libdecsync.so")#' | tr $'\r' $'\n' > __init__.py.new
mv __init__.py.new libdecsync/__init__.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto
mkdir -p %{buildroot}%{python3_sitelib}/%{_libPath}
ln -s %{_libdir}/libdecsync.so %{buildroot}%{python3_sitelib}/%{_libPath}/libdecsync.so
# not necessary for every package, but for those who it is, it'd generate conflict with others otherwise
rm -rf %{buildroot}%{python3_sitelib}/tests/

# %%check
# %%pyproject_check_import


%files -n python3-libdecsync -f %{pyproject_files}
%{python3_sitelib}/%{_libPath}/libdecsync.so

%changelog
%autochangelog
