Summary:	Football (soccer) manager game
Name:		bygfoot
Version:	2.3.2
Release:	7
License:	GPLv2+
Group:		Games/Sports
Url:		http://bygfoot.sourceforge.net
Source0:	http://downloads.sourceforge.net/bygfoot/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-2.2.1-gst-version.patch
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gtk+-2.0)

%description
Bygfoot is a small and simple football (a.k.a. soccer) manager game
featuring quite a few international leagues and cups. You manage a
team from one such league: you form the team, buy and sell players,
get promoted or relegated and of course try to be successful.

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO UPDATE ReleaseNotes
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}
%patch0 -p1

%build
export LDFLAGS="-lpthread -lm"
aclocal --force
autoconf --force
autoheader --force
touch configure.in
%configure2_5x \
	--enable-gstreamer

%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/{pixmaps,applications}
install -m 0644 support_files/pixmaps/bygfoot_icon.png %{buildroot}%{_datadir}/pixmaps/bygfoot.png
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


