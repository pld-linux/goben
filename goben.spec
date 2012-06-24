Summary:	GUI interface to Go playing programs
Summary(pl):	Graficzny interfejs dla program�w do gry w go
Name:		goben
Version:	0.1.1
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.waz.easynet.co.uk/misc/goben/%{name}-%{version}.tar.gz
# Source0-md5:	04c996c671ad70fda0e369867f58e4a5
Source1:	%{name}.desktop
URL:		http://www.waz.easynet.co.uk/software.html
Patch0:		%{name}-cflags.patch
Patch1:		%{name}-gnugo.patch
Patch2:		%{name}-home_etc.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
goben is a GUI frontend to GNU Go and other Go playing programs that
can talk GTP.

%description -l pl
goben dostarcza interfejsu graficznego do gry w go z GNU Go oraz
innymi programami obs�uguj�cymi protok� GTP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/goben,%{_desktopdir}}
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
