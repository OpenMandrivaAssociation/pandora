%define name pandora
%define version 0.9.3
%define release %mkrel 1

Summary: GIMP plugin for making panoramas
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://shallowsky.com/software/pandora/pandora-combine-%{version}.scm
License: GPL
Group: Graphics
Url: http://shallowsky.com/software/pandora/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgimp-devel >= 2.0
BuildArch: noarch

%description
This is a plugin for The Gimp that generates panorama images.

%package -n gimp2-pandora
Summary: GIMP plugin for making panoramas
Group: Graphics
Requires: gimp2_0

%description -n gimp2-pandora
This is a plugin for The Gimp that generates panorama images. This
version requires gimp 2.

%prep

%build

%install
rm -rf %{buildroot}
install -D -m 644 %SOURCE0 %{buildroot}$(gimptool-2.0 --gimpdatadir)/scripts/pandora-combine.scm


%clean
rm -rf %{buildroot}

%files -n gimp2-pandora
%defattr(-,root,root)
%_datadir/gimp/2.0/scripts/*

