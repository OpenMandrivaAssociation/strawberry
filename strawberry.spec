Summary:	Audio player and music collection organizer forked from Clementine (and Clementine from Amarok 1.4)
Name:		strawberry
Version:	1.0.1
License:	GPLv2 and GPLv3+ and LGPLv2 and ASL 2.0 and MIT and Boost
Group:		Sound
Url:		https://www.strawberrymusicplayer.org/
Source0:	https://github.com/strawberrymusicplayer/strawberry/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Release:	1

BuildRequires:	cmake
BuildRequires:	cmake(qt6)
BuildRequires:	qmake-qt6
BuildRequires:	boost-devel
BuildRequires:	liblastfm-devel
BuildRequires:	pkgconfig(cryptopp)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gstreamer-tag-1.0)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libchromaprint)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libplist-2.0)
# For Google Drive integration
BuildRequires:	pkgconfig(libsparsehash)
BuildRequires:	pkgconfig(libusbmuxd-2.0)
BuildRequires:	pkgconfig(protobuf) >= 3.3.2
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(taglib) >= 1.6
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:  qt6-qttools
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlite3)


Requires:	libprojectm-data
Requires:	%{_lib}qt5sql5-sqlite
Requires:	gstreamer-tools
Requires:	gstreamer%{gstapi}-flac
Requires:	gstreamer%{gstapi}-plugins-ugly
Requires:	gstreamer%{gstapi}-plugins-bad
Suggests:	gstreamer%{gstapi}-decoders-audio
# Needed to be able to mount ipod/iphone/ipad (not tested locally) but it's also pulling gvfs
# which is need at least to mount mtp devices (tested locally)
Suggests:	gvfs-iphone
# Need for listen music from some online sources like Google Drive or SoundCloud (bug 2133)
Recommends:	glib-networking

%description
Strawberry is a music player and music collection organizer. It is a fork of Clementine released in 2018 aimed at music collectors and audiophiles. 
It's written in C++ using the Qt toolkit.

%files
#config %{_sysconfdir}/Clementine/Clementine.conf
#{_bindir}/clementine
#{_bindir}/clementine-tagreader
#{_datadir}/kservices5/clementine-*.protocol
#{_datadir}/applications/clementine.desktop
#{_datadir}/metainfo/clementine.appdata.xml
#{_iconsdir}/hicolor/*/apps/clementine.*
#if %{with plf}
#{_bindir}/clementine-spotifyblob

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DBUILD_WERROR=OFF \
  -DBUILD_WITH_QT6=ON
    
%make_build

%install
%make_install -C build