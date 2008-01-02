Summary:	Bygfoot is a football (soccer) manager game
Name:		bygfoot
Version:	2.2.0
Release:	%mkrel 1
License:	GPL
Group:		Games/Sports
Url:		http://bygfoot.sourceforge.net
Source0:	http://downloads.sourceforge.net/bygfoot/%{name}-%{version}-source.tar.bz2
Source1:	%{name}.desktop
BuildRequires:	libgtk+2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Bygfoot is a small and simple football (a.k.a. soccer) manager game
featuring quite a few international leagues and cups. You manage a
team from one such league: you form the team, buy and sell players,
get promoted or relegated and of course try to be successful.

%prep
%setup -qn %{name}-%{version}-source

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std
mkdir -p %{buildroot}%{_datadir}/{pixmaps,applications}

install support_files/pixmaps/bygfoot_icon.png %{buildroot}%{_datadir}/pixmaps/bygfoot.png
install %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%post
%{update_menus}
%if %mdkversion >= 200700
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%postun
%{clean_menus}
%if %mdkversion >= 200700
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO UPDATE ReleaseNotes
%dir %{_datadir}/%{name}/support_files
%dir %{_datadir}/%{name}/support_files/definitions
%dir %{_datadir}/%{name}/support_files/lg_commentary
%dir %{_datadir}/%{name}/support_files/names
%dir %{_datadir}/%{name}/support_files/pixmaps/history
%dir %{_datadir}/%{name}/support_files/pixmaps/live_game
%dir %{_datadir}/%{name}/support_files/pixmaps/symbols
%dir %{_datadir}/%{name}/support_files/strategy
%dir %{_datadir}/%{name}/support_files/mmedia
%{_bindir}/%{name}
%{_datadir}/%{name}/support_files/bygfoot*
%{_datadir}/%{name}/support_files/definitions/*/*.xml
%{_datadir}/%{name}/support_files/lg_commentary/*.xml
%{_datadir}/%{name}/support_files/names/*.xml
%{_datadir}/%{name}/support_files/pixmaps/*.png
%{_datadir}/%{name}/support_files/pixmaps/*/*.png
%{_datadir}/%{name}/support_files/strategy/*.xml
%{_datadir}/%{name}/support_files/mmedia/pics/*.jpg
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
