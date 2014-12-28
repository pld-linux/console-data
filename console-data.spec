Summary:	Linux console data
Summary(pl.UTF-8):	Pliki danych dla konsoli
Name:		console-data
Version:	1999.08.29
Release:	4
License:	GPL
Group:		Applications/Console
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	b534787af0edaa73f608f518263f9334
Source1:	lat2u-16.psf.gz
# Source1-md5:	dc90a9bcff858175beea32a9b3bebb33
Source2:	lat2u.sfm.gz
# Source2-md5:	8ac4abc169fa1236fc3e64163c043113
URL:		http://lct.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains all data files (keymaps, fonts, misc tables)
that used to be part of the console-tools.

%description -l pl.UTF-8
Ten pakiet zawiera pliki danych dla konsoli (czcionki, mapy
klawiatury, różnorodne tablice), które kiedyś były częścią
console-tools.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-main_compressor=gzip
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -f %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/consolefonts/
cp -f %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/consoletrans/

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
