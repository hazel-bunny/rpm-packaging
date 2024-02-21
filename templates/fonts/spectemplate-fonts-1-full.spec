# Packaging template: less common patterns for single-family fonts packaging.
#
# SPDX-License-Identifier: MIT
#
# This template documents less common spec declarations, used when packaging a
# single font family, from a single dedicated source archive.
#
# It is part of the following set of packaging templates:
# “fonts-0-simple”: basic single-family fonts packaging
# “fonts-1-full”:   less common patterns for single-family fonts packaging
# “fonts-2-multi”:  multi-family fonts packaging
# “fonts-3-sub”:    packaging fonts, released as part of something else
#
Version:
Release:
URL:

%global foundry
%global fontlicense       OFL
#
# The following directives are lists of space-separated shell globs
#   – matching files associated with the font family,
#   – as they exist in the build root,
#   — at the end of the %build stage:
# – legal files (licensing…)
%global fontlicenses      OFL.txt
# – exclusions from the “fontlicenses” list
%global fontlicensesex
# – documentation files
%global fontdocs
# – exclusions from the “fontdocs” list
%global fontdocsex        %{fontlicenses}

%global fontfamily
%global fontsummary
# A container for additional subpackage declarations.
%global fontpkgheader     %{expand:
Obsoletes:
}
#
# More shell glob lists:
# – font family files
%global fonts
# – exclusions from the “fonts” list)
%global fontsex
# – fontconfig files
%global fontconfs         %{SOURCE10}
# – exclusions from the “fontconfs” list
%global fontconfsex
# – appstream files, if any (generated automatically otherwise)
%global fontappstreams
# – exclusions from the “fontappstreams” list
%global fontappstreamsex
#
%global fontdescription   %{expand:
}

Source0:
Source10: [number]-%{fontpkgname}.conf

%fontpkg

# Font creators love to bundle bulky documentation files, that show off their
# font (typically, as pdf specimens). Split those files in a dedicated optional
# doc package.
%package   doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
%setup
# Convert upstream files to UTF-8 and Unix end of lines if necessary
# Optional arguments:
# -e [encoding] source OS encoding (auto-detected otherwise)
# -n            do not recode files, only adjust folding and end of lines
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc *.pdf

%changelog
