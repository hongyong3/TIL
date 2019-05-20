[TOC]

## Add Comment with axios

### 0. Add Comment

- template
    - 댓글 form에 class만 추가해준다. 나머지 완전 그대로 둠!

        ```django
        <form action="{% url 'posts:comment_create' post.id %}" method="POST" class="comment-form">
          {% csrf_token %}
          <div class="input-group">
            {{ comment_form }}
            <div class="input-group-append">
              <button class="btn btn-primary" type="submit">Submit</button>
            </div>
          </div>
    </form>
        ```
    
- script
    - class를 바탕으로 모든 form을 불러와 이벤트리스너를 달아준다.
    - `event.preventDefault()`를 통해서 기본 동작을 막아준다. (form 태그를 통한 request를 막음.)
    - `new FormData(form)`을 통해서 form에 작성된 input들의 값을 모아 FormData 객체로 만들어 준다.
    - `axios.post()` 요청 첫번째 파라미터에 form.action(event.target.action과 같음), 두번째 파라미터에 FormData 객체를 넘겨준다.
        - 하나 중요한 점! `axios.post()` 도 POST 요청이니까 항상 쌍으로 다니는 csrf_token을 함께 보내야 한다. 이 친구는 이 코드에 어디에 있을까?
        - 바로 `FormData` 안에 이미 들어있다. → 왜? → 렌더링 된 form tag을 잘 생각해보라(혹은 template 파일 자체). csrf_token 데이터가 들어있는 hidden input이 함께 존재했다!
        - 그래서 여기서는 따로 설정해줄 필요 없다.

    
    ```javascript
    // list.html
    
    const commentForms = document.querySelectorAll('.comment-form')
    commentForms.forEach(function(form){
        form.addEventListener('submit', function(event){
            event.preventDefault()
            // event.target === form
            data = new FormData(event.target)
    				// Inspect FormData
    				for (let item of data.entries()) {
                console.log(item)
            }
            axios.post(event.target.action, data)
            .then(function(response){
    						comment = response.data
                const commentList = document.querySelector(`#comment-list-${comment.postId}`)
                newComment = `<div class="card-text">
                                <strong>${comment.username}</strong> ${comment.content}
                                <a href="/posts/${comment.postId}/comments/${comment.id}/delete/">
                                  <i class="fas fa-times"></i>
                                </a>
                              </div>`
                commentList.insertAdjacentHTML('beforeend', newComment)
                event.target.reset()
            })
    })
    })
    ```
    
- views.py
    - post id, comment id, comment 작성자(username), comment 내용(content)
    
- object 자체를 넘길 수 없으므로, 모두 string 형으로 전달해야함.
    
        ```python
        def comment_create(request, post_id):
        		...
        # return redirect('posts:list')
        		return JsonResponse({'postId': post_id, 'id': comment.id, 'username': comment.user.username, 'content': comment.content})
        ```
    
- template
    - 자연스러움을 위해 `{% empty %}` 부분을 날려버리자.

        ```django
        <!-- _post.html -->
        
        <div class="card-body" id="comment-list-{{ post.id }}">
          {% for comment in post.comment_set.all %}
            <div class="card-text">
              <strong>{{comment.user}}</strong> {{comment.content}}
              {% if comment.user == request.user %}
              <a href="{% url 'posts:comment_delete' post.id comment.id %}">
                <i class="fas fa-times"></i>
              </a>
              {% endif %}
            </div>
          {% endfor %}
        </div>
        ```
        
        