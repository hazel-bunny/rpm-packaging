# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate adblock

Name:           rust-adblock-angelfish
Version:        0.7.16
Release:        %autorelease
Summary:        Native Rust module for Adblock Plus syntax

License:        MPL-2.0
URL:            https://crates.io/crates/adblock
Source:         %{crates_source}

Patch:          adblock-disable-benchmarks.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Native Rust module for Adblock Plus syntax (e.g. EasyList, EasyPrivacy)
filter parsing and matching.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+embedded-domain-resolver-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+embedded-domain-resolver-devel %{_description}

This package contains library source intended for building other packages which
use the "embedded-domain-resolver" feature of the "%{crate}" crate.

%files       -n %{name}+embedded-domain-resolver-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+full-regex-handling-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+full-regex-handling-devel %{_description}

This package contains library source intended for building other packages which
use the "full-regex-handling" feature of the "%{crate}" crate.

%files       -n %{name}+full-regex-handling-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+object-pooling-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+object-pooling-devel %{_description}

This package contains library source intended for building other packages which
use the "object-pooling" feature of the "%{crate}" crate.

%files       -n %{name}+object-pooling-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -f embedded-domain-resolver,full-regex-handling,object-pooling

%build
%cargo_build -f embedded-domain-resolver,full-regex-handling,object-pooling

%install
%cargo_install -f embedded-domain-resolver,full-regex-handling,object-pooling

%if %{with check}
%check
%cargo_test -f embedded-domain-resolver,full-regex-handling,object-pooling
%endif

%changelog
%autochangelog
