# BFS
 - BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
 - 맹목적인 탐색을 하고자할 때 사용할 수 있는 기본적인 탐색 기법
 - 최단 경로를 찾아준다는  점에서 최단길이를 보장해야 할 때 많이 사용(미로 찾기)
 - 큐 자료구조를 이용
  - 탐색 시작 노드를 큐에 삽입하고 방문 처리
  - 큐에서 노드를 꺼낸 뒤, 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
  - 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
 - 큐

 - 파이썬 deque
   - 스택과 큐의 기능을 모두 가짐 / 출입구를 양쪽에 가지고 있음 -> 스택처럼 써도 되고, 큐처럼 써도 된다.
   - deque 생성
   - ```
     >>> from collections import deque
     >>> dq=deque('abcd')
     >>> dq
     deque(['a','b','c','d'])
     ``` 

   - 스택구현 : append(), pop()
   - 입력시에는 append()메서드 사용, 출력시에는 pop()이용
   - ```
      >>> dq.append('m')                       # 오른쪽 끝에 항목추가
      >>> dq
      deque(['a', 'b', 'c', 'd', 'm'])
      >>> dq.pop()                             # 오른쪽 끝에 항목가져오면서 삭제
      'm'
      >>> dq
      deque(['a', 'b', 'c', 'd']) 
     ```
  
   - 큐 구현 : appendleft(),pop(),append(),popleft()
   - 큐는 왼쪽에서 입력되고, 오른쪽에서 출력된다.
   - 오른쪽 출력 시는 pop()이용
   - 왼쪽에 값을 입력 시에는 appendleft()메서드 사용
   - ```
     >>> dq.appendleft('I')                   # 왼쪽에서 'I'입력
     >>> dq
     deque(['I', 'a', 'b', 'c', 'd'])
     >>> dq.pop()                             # 오른쪽에서 'e'출력
     'd'
     >>> dq
     deque(['I', 'a', 'b', 'c']) 

     ```
  
   - 확장 : extend(), extendleft()
   - 기본적으로 오른쪽으로 확장
   - 왼쪽으로 확장하고 싶으면 extendleft()이용
   - ```
     >>> dq
     deque(['a', 'b', 'c', 'd'])
     >>> dq.extend('you')                            # 오른쪽으로 'y','o','u' 확장
     >>> dq
     deque(['a', 'b', 'c', 'd', 'y', 'o', 'u'])
     >>> dq.extendleft('I')                          # 왼쪽으로 'I' 확장
     >>> dq
     deque(['I', 'a', 'b', 'c', 'd', 'y', 'o', 'u']) 

     ```
  
   - 리스트처럼 사용 : insert(),remove()
   - 리스트처럼 중간내용을 수정하거나 새 항목을 입력하거나 삭제할 수 있다.
   - ```
     >>> dq
     deque(['a', 'b', 'c', 'd'])
     >>> dq[2]='n'                      # 인덱스를 이용한 항목 수정 'b' => 'n'
     >>> dq
     deque(['a', 'b', 'n', 'd']) 
     
     ```
   - 새 항목을 입력하거나 기본 항목을 삭제할 때는 insert()메서드와 remove()메서드를 사용한다.
   - ```
      >>> dq = deque('abcd')
      >>> dq.insert(0, 'K')                         # 첫번째 항목에 'K'를 추가
      >>> dq
      deque(['K', 'a', 'b', 'c', 'd'])         
      >>> dq.insert(100, 'K')                       # 100번째 항목(없으니까 가장 큰 쪽에)에 'K' 추가
      >>> dq
      deque(['K', 'a', 'b', 'c', 'd', 'K'])  
      >>> dq.remove('K')                            # 'K'항목 삭제
      >>> dq
      deque(['a', 'b', 'c', 'd', 'K'])              # 같은 항목이 있을때 지우면 왼쪽부터 삭제됨.
      >>> dq.remove('K')
      >>> dq
      deque(['a', 'b', 'c', 'd'])                   # 오른쪽에 있는 'K'삭제
     ```
  
   - 반전 : reverse()

