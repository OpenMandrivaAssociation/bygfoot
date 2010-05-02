Summary:	Football (soccer) manager game
Name:		bygfoot
Version:	2.3.2
Release:	%mkrel 2
License:	GPLv2+
Group:		Games/Sports
Url:		http://bygfoot.sourceforge.net
Source0:	http://downloads.sourceforge.net/bygfoot/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-2.2.1-gst-version.patch
BuildRequires:	libgtk+2-devel
BuildRequires:	gstreamer0.10-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Bygfoot is a small and simple football (a.k.a. soccer) manager game
featuring quite a few international leagues and cups. You manage a
team from one such league: you form the team, buy and sell players,
get promoted or relegated and of course try to be successful.

%prep
%setup -qn %{name}-%{version}
%patch0 -p1

%build
aclocal --force
autoconf --force
autoheader --force

%configure2_5x \
	--enable-gstreamer

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std
mkdir -p %{buildroot}%{_datadir}/{pixmaps,applications}

install -m 0644 support_files/pixmaps/bygfoot_icon.png %{buildroot}%{_datadir}/pixmaps/bygfoot.png
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO UPDATE ReleaseNotes
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
