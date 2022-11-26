# Assignment 5

제출기한: 2022-12-23 (금) 23:59:59


## the last test case 통과하기
[./waffle/tests.py](./waffle/test.py)의 TODO 부분을 수정하여, test를 통과하도록 해주세요.

```shell
python manage.py test
```

- 제출방법: 해당 repository를 fork 한 후 PR 날려주시면 됩니다.

---

## load_data command (참고)

테스트에서는 테스트 db를 새로 생성하기 때문에 사용하지 않지만, views들을 테스트하고 싶을 때 사용할 수 있는 load_waffle command가 준비되어 있습니다.

```shell
python manage.py migrate  # DB 생성
python manage.py load_waffle  # 데이터 로딩
```


