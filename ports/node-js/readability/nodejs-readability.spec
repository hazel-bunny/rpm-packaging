%global npm_name readability

Name:           nodejs-%{npm_name}
Version:        0.4.4
Release:        1%{?dist}
Summary:        Library used for Firefox Reader View
License:        Apache-2.0

URL:            https://github.com/mozilla/readability
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source2:        %{npm_name}-%{version}-nm-dev.tgz
Source3:        %{npm_name}-%{version}-bundled-licenses.txt

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

Requires:       nodejs
BuildRequires:  nodejs-devel

%description
%{summary}.


%prep
%setup -q -n package
cp %{SOURCE3} .
# Setup bundled runtime(prod) node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json index.js lib/ \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{nodejs_sitelib}/tape/bin
install -p -D -m0755 bin/tape %{buildroot}%{nodejs_sitelib}/tape/bin/tape
mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/tape/bin/tape %{buildroot}%{_bindir}/tape

%check
%{__nodejs} -e 'require("./")'
# Setup bundled dev node_modules for testing
#   Note: this cannot be in %%prep or the dev node_modules
#            can get pulled into the regular rpm
tar xfz %{SOURCE2}
pushd node_modules
ln -s ../node_modules_dev/* .
popd
pushd node_modules/.bin
ln -s ../../node_modules_dev/.bin/* .
popd
# Run tests
./node_modules/.bin/tap test/*.js


%files
%doc readme.markdown
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/tape
%{_bindir}/tape


%changelog
