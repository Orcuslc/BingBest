INCFLAGS = -I /usr/local/qt5/include
INCFLAGS += -I /usr/local/qt5/include/QtCore

LINKFLAGS = -L /usr/local/qt5/lib -lQt5Core


CC = g++
CFLAGS = -ansi -std=c++11 -fPIC
SRCS = test.cpp
OBJS = $(SRCS:.cpp=.o)
PROG = version

all: $(SRCS) $(PROG)

$(PROG): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $@ $(LINKFLAGS)

.cpp.o:
	$(CC) $(CFLAGS) $< -c -o $@ $(INCFLAGS)

depend:
	makedepend $(INCFLAGS) -Y $(SRCS)

clean:
	rm $(OBJS) $(PROG)