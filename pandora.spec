Summary:	GIMP plugin for making panoramas
Name:		pandora
Version:	0.9.3
Release:	4
License:	GPL
Group:		Graphics
Url:		http://shallowsky.com/software/pandora/
Source0:	http://shallowsky.com/software/pandora/pandora-combine-%{version}.scm
BuildRequires:	gimp-devel >= 2.0
BuildArch:	noarch

%description
This is a plugin for The Gimp that generates panorama images.

%package -n gimp2-pandora
Summary:	GIMP plugin for making panoramas
Group:		Graphics
Requires:	gimp

%description -n gimp2-pandora
This is a plugin for The Gimp that generates panorama images. This
version requires gimp 2.

%prep

%build

%install
install -D -m 644 %SOURCE0 %{buildroot}$(gimptool-2.0 --gimpdatadir)/scripts/pandora-combine.scm

%files -n gimp2-pandora
%{_datadir}/gimp/2.0/scripts/*

