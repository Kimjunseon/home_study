# Mini conda 설정
1. Path: 사용자이름  - script 
2. 경로 저장
3. 시스템 변수 Path 설정해주기

4. 기본 설정

4.1 Window Powershell 기입(관리자권한)

    Set-ExecutionPolicy RemoteSigned 권한을 주기?

4.2 Anaconda Powershell Prompt 기입

    conda init powershell: 윈도우 파워셀에 콘다 설정하기
   
4.3 Window Powershell 기입

    conda config --set auto_activate_base False: 윈도우 실행 시 자동켜짐 끄기

# 콘다 명령어, Window Powershell에 기입

* 콘다 활성화하기

      conda activate or conda activate ~~~ : ~~~ 을 파일폴더명을 가진 env 활성화

* 현재 환경유무 확인

      conda env list

* 현재 설치된 모듈리스트 보기

      conda list

* 가상환경 만들기

      conda create -n ~~~ python=3.8: 파이썬버전이 3.8인 ~~~ 이름의 가진 가상환경 만들기

* 넘파이 설치

      conda install numpy

* 판다스 설치

      conda install pandas

* matplotlib 설치

      conda install matplotlib

* 쥬피터 설치

      conda install jupyter

* 해당폴더에 주피터 생성 후 실행

      jupyter notebook

* 쥬피터 노트북 폰트 설정

      1. jupyter notebook --generate-config: 쥬피터 일반적인 설정 파일 만들기
      2. 사용자 폴더 아래 jupyter에 custom 폴더, 안에 custom.css 만들기

```
--공백이 없는 사이트 설정--
.container { width: 100% !important;}
div.CodeMirror, dic.output_area pre, div.ouput_wrapper pre{
  font-family: Source Code Pro;
  font-size: 19pt;
  line-height: 110%
}
div#notebook, div.prompt{
    font-family: Source Code Pro;
    font-size: 19pt;
    line-height: 110%;
}
```

* 색깔 사이트

        https://matplotlib.org/stable/gallery/color/named_colors.html

