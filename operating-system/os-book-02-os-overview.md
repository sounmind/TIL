# 책 2장 | 운영체제 개요

# 1. 운영체제의 정의

운영체제란 컴퓨터 하드웨어 바로 윗단에 설치되는 소프트웨어를 말한다. 운영체제는 사용자 및 다른 모든 소프트웨어와 하드웨어를 연결하는 소프트웨어 계층으로 그 위상은  아래 그림과 같다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/380098f9-e961-4129-b8e0-8434202841d8/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/380098f9-e961-4129-b8e0-8434202841d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201110T164126Z&X-Amz-Expires=86400&X-Amz-Signature=30540618faf18665870c0e9ab258b74c2b9c94e7ef88c6bc5a67aa5e71d57b48&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

운영체제(Operating System)의 System이라는 용어는 기반이나 틀이 되는 하드웨어를 지칭할 때 주로 사용되는데, 소프트웨어인 운영체제에 시스템이라는 용어가 사용된 것은 하드웨어가 운영체제와 한 몸이 되어야만 사용자에게 쓰일 수 있는 진정한 컴퓨터 시스템이 되기 때문이다.

컴퓨터의 전원을 켜면 운영체제는 이와 동시에 실행된다. 한편 소프트웨어가 컴퓨터 시스템에서 실행되기 위해서는 메모리에 그 프로그램이 올라가 있어야 한다. 운영체제 자체도 하나의 소프트웨어로서 전원이 켜짐과 동시에 메모리에 올라간다. 하지만 운영체제처럼 규모가 큰 프로그램이 모두 메모리에 올라간다면 한정된 메모리 공간의 낭비가 심할 것이다. 따라서 운영체제 중 항상 필요한 부분(커널)만을 전원이 켜짐과 동시에 메모리에 올려놓고 그렇지 않은 부분(파일 복사 등과 같은 프로그램)은 필요할 때 메모리로 올려서 사용하게 된다.

# 2. 운영체제의 기능

운영체제의 역할은 하드웨어를 역할과 사용자를 위한 역할의 두 가지로 나눠볼 수 있다. 자세히 말하자면, 컴퓨터 시스템 내의 자원을 효율적으로 관리하는 것과 컴퓨터 시스템을 편리하게 사용할 수 있는 환경을 제공하는 것이다.

운영체제는 사용자 및 프로그램들 간에 자원이 형평성 있게 분배되도록 하는 균형자 역할도 함께 수행해야 한다. 즉, 효율성이 가장 큰 목표이지만 이로 인해 일부가 지나치게 희생되지 않게 하는 형평성 역시 운영체제가 고려해야 할 목표이다.

이 밖에도, 운영체제는 사용자와 운영체제 자신을 보호하는 역할을 담당한다. 여러 사용자의 프로그램이 하나의 컴퓨터에서 실행되면 이에 대한 보안이 필요하다. → 보안 및 보호 기능을 수행하게 된다.