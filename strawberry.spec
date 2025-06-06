Summary:	Audio player and music collection organizer forked from Clementine (and Clementine from Amarok 1.4)
Name:		strawberry
Release:	1
Version:	1.2.11
License:	GPLv2 and GPLv3+ and LGPLv2 and ASL 2.0 and MIT and Boost
Group:		Sound
Url:		https://www.strawberrymusicplayer.org/
Source0:	https://github.com/strawberrymusicplayer/strawberry/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	cmake(qt6)
BuildRequires:	qmake-qt6
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gstreamer-tag-1.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gtest)
BuildRequires:	pkgconfig(icu-io)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libchromaprint)
BuildRequires:	pkgconfig(libebur128)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libplist-2.0)
BuildRequires:	pkgconfig(libusbmuxd-2.0)
BuildRequires:	pkgconfig(libsparsehash)
BuildRequires:	pkgconfig(libvlc)
BuildRequires:	pkgconfig(protobuf) >= 3.3.2
BuildRequires:	pkgconfig(RapidJSON)
BuildRequires:	pkgconfig(taglib) >= 1.11.1
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:	qt6-qtbase-sql-firebird
BuildRequires:	qt6-qtbase-sql-mariadb
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Linguist)
BuildRequires:	cmake(absl)
BuildRequires:	cmake(KDSingleApplication-qt6)
BuildRequires:	qt6-qttools
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	vulkan-headers
BuildRequires:	ninja

Requires:	gstreamer-tools
Requires:	gstreamer1.0-flac
Requires:	gstreamer1.0-plugins-ugly
Requires:	gstreamer1.0-plugins-bad
Suggests:	gstreamer1.0-decoders-audio
# Needed to be able to mount ipod/iphone/ipad (not tested locally) but it's also pulling gvfs
# which is need at least to mount mtp devices (tested locally)
Suggests:	gvfs-iphone
# Need for listen music from some online sources like Google Drive or SoundCloud (bug 2133)
Recommends:	glib-networking

%description
Strawberry is a music player and music collection organizer. It is a fork of Clementine released in 2018 aimed at music collectors and audiophiles. 
It's written in C++ using the Qt toolkit.

%files
%{_bindir}/strawberry
%{_datadir}/applications/org.strawberrymusicplayer.strawberry.desktop
%{_iconsdir}/hicolor/*x*/apps/strawberry.png
%{_datadir}/metainfo/org.strawberrymusicplayer.strawberry.appdata.xml
%{_mandir}/man1/strawberry.1.*
#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}
# Needed for absl >= 202401
sed -i -e 's,CMAKE_CXX_STANDARD 17,CMAKE_CXX_STANDARD 20,;s,c++17,c++20,g' CMakeLists.txt

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DBUILD_WERROR=OFF \
	-DBUILD_WITH_QT6=ON \
	-G Ninja
    
%ninja_build

%install
%ninja_install -C build
