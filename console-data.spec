Summary:        Linux console data
Summary(pl):    Pliki danych dla konsoli
Name:           console-data
Version:        1999.08.29
Release:        1
Copyright:      GPL
Group:          Utilities/Console
Group(pl):      Narz�dzia/Konsola
Source0:	http://www.multimania.com/ydirson/soft/lct/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This package contains all data files (keymaps, fonts, misc tables) 
that used to be part of the console-tools.

%description -l pl
Ten pakiet zawiera pliki danych dla konsoli (czcionki, mapy klawiatury,
r�znorodne tablice), kt�re kiedy� by�y cz�ci� console-tools.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
        --with-main_compressor=gzip
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf doc/{fonts/*,keymaps/*,README*} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{fonts,keymaps,README*} 

%{_datadir}/consolefonts
%{_datadir}/consoletrans
%{_datadir}/keymaps
%{_datadir}/unidata
