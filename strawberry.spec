Summary:	Audio player and music collection organizer forked from Clementine
Name:		strawberry
Version:	1.2.19
Release:	1
License:	GPLv2 and GPLv3+ and LGPLv2 and ASL 2.0 and MIT and Boost
Group:	Sound
Url:		https://www.strawberrymusicplayer.org/
Source0:	https://github.com/strawberrymusicplayer/strawberry/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake >= 3.13
BuildRequires:	ninja
BuildRequires:	qmake-qt6
BuildRequires:	qt6-qtbase-sql-firebird
BuildRequires:	qt6-qtbase-sql-mariadb
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:	qt6-qttools
BuildRequires:	qt6-qttools-linguist-tools
BuildRequires:	vulkan-headers
BuildRequires:	boost-devel
BuildRequires:	cmake(absl)
BuildRequires:	cmake(KDSingleApplication-qt6)
BuildRequires:	cmake(qt6)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Core) >= 6.4.0
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Linguist)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-app-1.0)
BuildRequires:	pkgconfig(gstreamer-audio-1.0)
BuildRequires:	pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gstreamer-tag-1.0)
BuildRequires:	pkgconfig(gtest)
BuildRequires:	pkgconfig(icu-io)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libchromaprint) >= 1.4
BuildRequires:	pkgconfig(libebur128)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libplist-2.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libusbmuxd-2.0)
BuildRequires:	pkgconfig(libsparsehash)
BuildRequires:	pkgconfig(libvlc)
BuildRequires:	pkgconfig(protobuf) >= 3.3.2
BuildRequires:	pkgconfig(RapidJSON)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(taglib) >= 1.12
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xkbcommon)

Requires:	gstreamer-tools
Requires:	gstreamer1.0-flac
Requires:	gstreamer1.0-plugins-ugly
Requires:	gstreamer1.0-plugins-bad
Suggests:	gstreamer1.0-decoders-audio
# Needed to be able to mount ipod/iphone/ipad (not tested locally) but it's also pulling gvfs
# which is needed at least to mount mtp devices (tested locally)
Suggests:	gvfs-iphone
# Need for listen music from some online sources like Google Drive or SoundCloud (bug #2133)
Recommends:	glib-networking

%description
Strawberry is a music player and music collection organizer. It is a fork
of Clementine (and Clementine was a fork of Amarok 1.4), released in 2018
and aimed at music collectors and audiophiles.
It's written in C++ using the Qt toolkit.

%files
%{_bindir}/%{name}
%{_datadir}/applications/org.strawberrymusicplayer.%{name}.desktop
%{_iconsdir}/hicolor/*x*/apps/%{name}.png
%{_datadir}/metainfo/org.strawberrymusicplayer.%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}

# Needed for absl >= 202401
sed -i -e 's,CMAKE_CXX_STANDARD 17,CMAKE_CXX_STANDARD 20,;s,c++17,c++20,g' CMakeLists.txt


%build
#	-DBUILD_WITH_QT6=ON \
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DBUILD_WERROR=OFF \
	-DINSTALL_TRANSLATIONS=OFF \
	-G Ninja
    
%ninja_build


%install
%ninja_install -C build

