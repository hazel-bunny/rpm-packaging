Name:           python-protobuf
Version:        5.28.2
Release:        1%{?dist}
Summary:        Python bindings for Google Protocol Buffers
License:        BSD-3-Clause
URL:            https://developers.google.com/protocol-buffers/
Source:         %{pypi_source protobuf}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This package contains Python libraries for Google Protocol Buffers}

%description %_description

%package -n     python3-protobuf
Summary:        %{summary}

%description -n python3-protobuf %_description


%prep
%autosetup -p1 -n protobuf-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google


%check
%pyproject_check_import


%files -n python3-protobuf -f %{pyproject_files}
%{python3_sitearch}/protobuf-%{version}-py%{python3_version}-nspkg.pth

%changelog
* Thu Oct 17 2024 Hazel Bunny <hazel_bunny@disroot.org> - 5.28.2-1
- Initial package.
