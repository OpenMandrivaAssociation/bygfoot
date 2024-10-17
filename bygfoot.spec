Summary:	Football (soccer) manager game
Name:		bygfoot
Version:	2.3.5
Release:	1
License:	GPLv2+
Group:		Games/Sports
Url:		https://bygfoot.sourceforge.net
Source0:        https://gitlab.com/bygfoot/bygfoot/-/archive/%{version}/bygfoot-%{version}.tar.bz2
#Source0:	http://downloads.sourceforge.net/bygfoot/%{name}-%{version}.tar.bz2
#Source1:	%{name}.desktop
#Patch0:		%{name}-2.2.1-gst-version.patch
Patch0:         bygfoot-c99-1.patch
Patch1:         bygfoot-c99-2.patch
BuildRequires:  cmake ninja
BuildRequires:	gettext
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(json-c)

%description
Bygfoot is a small and simple football (a.k.a. soccer) manager game
featuring quite a few international leagues and cups. You manage a
team from one such league: you form the team, buy and sell players,
get promoted or relegated and of course try to be successful.

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO UPDATE ReleaseNotes
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake \
	-G Ninja
%ninja_build

%install
%ninja_install -C %{_vpath_builddir}

# .desktop file
install -dm 0755 %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Bygfoot
Comment=A football manager
Exec=%{name}
Icon=%{name}
Type=Application
Terminal=false
Categories=Game;SportsGame;
StartupNotify=false
Categories=Game;SportsGame;
X-Vendor=OpenMandriva
EOF

# icons
for d in 16 32 48 64 72 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	convert -background none -size "${d}x${d}" support_files/pixmaps/%{name}_icon.png \
			%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -size 32x32 support_files/pixmaps/%{name}_icon.png \
	%{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# locales
%find_lang %{name}


