Summary:	Linux console data
Summary(pl):	Pliki danych dla konsoli
Name:		console-data
Version:	1999.08.29
Release:	4
License:	GPL
Group:		Applications/Console
Source0:	http://altern.org/ydirson/soft/lct/%{name}-%{version}.tar.gz
Source1:	lat2u-16.psf.gz
Source2:	lat2u.sfm.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	autoconf
BuildRequires:	automake

%description
This package contains all data files (keymaps, fonts, misc tables)
that used to be part of the console-tools.

%description -l pl
Ten pakiet zawiera pliki danych dla konsoli (czcionki, mapy
klawiatury, róznorodne tablice), które kiedy¶ by³y czê¶ci±
console-tools.

%prep
%setup -q

%build
aclocal
autoconf
automake -a -c
%configure \
	--with-main_compressor=gzip
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -f %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/consolefonts/
cp -f %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/consoletrans/

gzip -9nf doc/{fonts/*,keymaps/*,README*} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{fonts,keymaps,README*} 

%{_datadir}/consolefonts
%{_datadir}/consoletrans
%{_datadir}/unidata

%dir %{_datadir}/keymaps
%{_datadir}/keymaps/include
%ifarch m68k
%{_datadir}/keymaps/amiga
%{_datadir}/keymaps/atari
%endif

%ifarch %ix86
%{_datadir}/keymaps/i386
%endif

%ifarch sparc sparc64
%{_datadir}/keymaps/sun
%endif

%ifarch m68k ppc
%{_datadir}/keymaps/mac
%endif
