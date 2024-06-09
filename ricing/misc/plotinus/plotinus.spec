Name:              plotinus

%global forgeurl https://github.com/fkloft/%{name}
%global commit c51aa596b4f92ec98baad4e20c659592369527a3
%global date 20180124
%forgemeta

Version:           0.2.0
Release:           1%{?dist}
Epoch:             1
Summary:           A searchable command palette in every modern GTK+ application
License:           WTFPL-1.0
URL:               %{forgeurl}
Source:            %{forgesource}

BuildRequires:     cmake
BuildRequires:     vala
BuildRequires:     gtk3-devel

%description
Have you used Sublime Text's or Atom's "Command Palette"? It's a list of
everything those editors can do that opens at the press of a key and finds the
action you are looking for just by typing a few letters. It's raw power at your
fingertips.

Plotinus brings that power to every application on your system (that is, to
those that use the GTK+ 3 toolkit). It automatically extracts all available
commands by introspecting a running application, instantly adapting to UI
changes and showing only relevant actions. Using Plotinus requires no
modifications to the application itself!

Just press Ctrl+Shift+P (configurable) and you're in business – it feels so
natural you'll soon wonder how you ever lived without it.

%prep
%forgeautosetup
sed -i 's,LIBRARY DESTINATION lib,LIBRARY DESTINATION %{_libdir},' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%check
#nothing

%files
%doc README.md
%{_bindir}/plotinus
%{_libdir}/libplotinus.so
%{_datadir}/glib-2.0/schemas/com.worldwidemann.plotinus.gschema.xml

%changelog
%autochangelog
