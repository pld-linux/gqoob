Summary:	Media player.
Summary(pl):	Odtwarzacz multimediów
Name:		gqoob
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://twtelecom.dl.sourceforge.net/sourceforge/gqmpeg/%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://gqmpeg.sourceforge.net

BuildRequires:	gtk+2 >= 2.0.2
Requires:	xine-lib >= 0.9.13

%define		_prefix		/usr/X11R6

%description
GQoob is a slightly configurable media player that uses the XINE
library.

%description -l pl
GQoob jest czê¶ciowo konfigurowalnym odtwarzaczem bazuj±cym 
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/applications
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install gqoob.desktop $RPM_BUILD_ROOT%{_datadir}/applications
install gqoob.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%doc README COPYING TODO SKIN-SPECS
%attr(755,root,root) %{_bindir}/gqoob
%{_datadir}/gqoob/*
%{_datadir}/locale/*/*/*
%{_datadir}/applications
%{_datadir}/pixmaps/gqoob.png
%{_mandir}/man?/*
