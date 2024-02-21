# Packaging template: packaging fonts, released as part of something else
#
# SPDX-License-Identifier: MIT
#
# This template documents spec declarations, used when packaging one or several
# font families from a source rpm which is not named after the first packaged
# font family:
# – either because the project name differs from the main font family name
# – or when the source archive and rpm are used to package more than fonts.
#
# It is part of the following set of packaging templates:
# “fonts-0-simple”: basic single-family fonts packaging
# “fonts-1-full”:   less common patterns for single-family fonts packaging
# “fonts-2-multi”:  multi-family fonts packaging
# “fonts-3-sub”:    packaging fonts, released as part of something else
#
# The packaging style is identical to the one documented in “fonts-2-multi”,
# EXCEPT it should not use the zero/nosuffix declaration block, as this block
# will attempt to generate source rpm declarations by default.
#
# Usually appropriate for fonts-only packages
BuildArch: noarch

Version:
Release:
License:
URL:

%global foundry
# If different from the main License
%global fontlicense
%global fontlicenses
%global fontlicensesex
%global fontdocs
%global fontdocsex        %{fontlicenses}

%global common_description %{expand:
}

%global fontfamily1
%global fontsummary1
%global fontpkgheader1    %{expand:
}
%global fonts1
%global fontsex1
%global fontconfs1        %{SOURCE11}
%global fontconfsex1
%global fontappstreams1
%global fontappstreamsex1
%global fontdescription1  %{expand:
%{common_description}
Additional text…}

%global fontfamily2
%global fontsummary2
%global fontpkgheader2    %{expand:
}
%global fonts2
%global fontsex2
%global fontconfs2        %{SOURCE12}
%global fontconfsex2
%global fontappstreams2
%global fontappstreamsex2
%global fontdescription2  %{expand:
%{common_description}
Other Additional text…}
#
# Continue as necessary…

Source0:
Source11: [number]-%{fontpkgname1}.conf
Source12: [number]-%{fontpkgname2}.conf

Name:
Summary:
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%package   doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
%setup
%linuxtext *.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%files doc
%defattr(644, root, root, 0755)
%license
%doc

%changelog
