Name:           python-radicale-storage-decsync
Version:        2.1.0
Release:        %autorelease
Summary:        DecSync storage plugin for Radicale

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-3.0-or-later
URL:            https://github.com/39aldo39/Radicale-DecSync
Source:         %{pypi_source radicale_storage_decsync}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  libdecsync-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'radicale_storage_decsync' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-radicale-storage-decsync
Summary:        %{summary}

%description -n python3-radicale-storage-decsync %_description


%prep
%autosetup -p1 -n radicale_storage_decsync-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-radicale-storage-decsync -f %{pyproject_files}


%changelog
%autochangelog
