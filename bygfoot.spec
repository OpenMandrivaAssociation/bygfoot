Summary:	Football (soccer) manager game
Name:		bygfoot
Version:	2.3.2
Release:	5
License:	GPLv2+
Group:		Games/Sports
Url:		http://bygfoot.sourceforge.net
Source0:	http://downloads.sourceforge.net/bygfoot/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-2.2.1-gst-version.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	gstreamer0.10-devel

%description
Bygfoot is a small and simple football (a.k.a. soccer) manager game
featuring quite a few international leagues and cups. You manage a
team from one such league: you form the team, buy and sell players,
get promoted or relegated and of course try to be successful.

%prep
%setup -qn %{name}-%{version}
%patch0 -p1

%build
export LDFLAGS="-lpthread -lm"
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


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.2-3mdv2011.0
+ Revision: 610089
- rebuild

* Sun May 02 2010 Funda Wang <fwang@mandriva.org> 2.3.2-2mdv2010.1
+ Revision: 541574
- fix perms

* Sun Jul 12 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.3.2-1mdv2010.0
+ Revision: 395065
- update to new version 2.3.2

* Mon Nov 17 2008 Funda Wang <fwang@mandriva.org> 2.3.0-1mdv2009.1
+ Revision: 303970
- New version 2.3.0

* Sat Jun 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2.1-1mdv2009.0
+ Revision: 229718
- update to new version 2.2.1
- Patch0: fix gstreamer version
- enable gstreamer backend
- do not package COPYING file

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.2.0-2mdv2008.1
+ Revision: 170779
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2.0-1mdv2008.0
+ Revision: 52712
- fix file list
- new version
- drop X-MandrivaLinux from desktop file


* Thu Feb 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.1.0-1mdv2007.0
+ Revision: 124690
- Import bygfoot

