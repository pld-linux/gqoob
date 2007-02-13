Summary:	Media player
Summary(pl.UTF-8):	Odtwarzacz multimediów
Name:		gqoob
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gqmpeg/%{name}-%{version}.tar.gz
# Source0-md5:	1949a0b17d0d52bfefab0458b6664af4
Patch0:		%{name}-desktop.patch
URL:		http://gqmpeg.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2 >= 2.0.2
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	xine-lib-devel >= 0.9.13
Requires:	xine-lib >= 0.9.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GQoob is a slightly configurable media player that uses the XINE
library.

%description -l pl.UTF-8
GQoob jest częściowo konfigurowalnym odtwarzaczem bazującym
na bibliotece XINE.

%prep
%setup -q
%patch0 -p1

%build
glib-gettextize --copy --force
intltoolize
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install gqoob.desktop $RPM_BUILD_ROOT%{_desktopdir}
install gqoob.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO SKIN-SPECS
%attr(755,root,root) %{_bindir}/gqoob
%{_datadir}/gqoob
%{_desktopdir}/*.desktop
%{_pixmapsdir}/gqoob.png
%{_mandir}/man?/*
