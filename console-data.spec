Summary:        Linux console data
Summary(pl):    Pliki danych dla konsoli
Name:           console-data
Version:        1999.04.15
Release:        1
Copyright:      GPL
Group:          Utilities/Console
Group(pl):      Narzêdzia/Konsola
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/keyboards/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This package contains all data files (keymaps, fonts, misc tables) 
that used to be part of the console-tools.

%description -l pl
Ten pakiet zawiera pliki danych dla konsoli (czcionki, mapy klawiatury,
róznorodne tablice), które kiedy¶ by³y czê¶ci± console-tools.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
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

%changelog
* Thu Apr 22 1999 Piotr Czerwiñski <pius@pld.org.pl>
- initial rpm release.
