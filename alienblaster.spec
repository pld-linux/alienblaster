Summary:	Shooting arcade game
Summary(pl.UTF-8):	Zręcznościowa strzelanka
Name:		alienblaster
Version:	1.1.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.informatik.uni-bremen.de/~schwardt/alienblaster/%{name}-%{version}.tgz
# Source0-md5:	27412a868f7d4ae0949036aeb29a6691
Source1:	%{name}.xpm
Source2:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
URL:		http://www.schwardtnet.de/alienblaster/
BuildRequires:	SDL-devel >= 1.2.7
BuildRequires:	SDL_mixer >= 1.2.5
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The game goal is to stop the invasion of the aliens and blast them.

%description -l pl.UTF-8
Celem gry jest powstrzymanie inwazji obcych i zniszczenie ich.

%prep
%setup -q -n %{name}
%patch -P0 -p1
%{__sed} -i 's@images@%{_datadir}/%{name}/images@' cfg/{level1.cfg,level2.cfg}
%{__sed} -i 's@.//@/@' cfg/{level1.cfg,level2.cfg}
%{__sed} -i 's@./images@%{_datadir}/%{name}/images@' src/{global.cc,global.h}
%{__sed} -i 's@./sound@%{_datadir}/%{name}/sound@' src/global.h
%{__sed} -i 's@./cfg@%{_datadir}/%{name}/cfg@' src/global.h

%build
%{__make} \
	COMPILER="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install alienBlaster $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -r {images,sound,cfg} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
