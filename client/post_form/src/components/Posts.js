

const Posts = ({posts}) => {

    console.log(posts);
    return (
        <div>
            <h1>Data</h1>
                {posts.map((post, id) => (
            <div key ={id}>
                    <h1>{post.title}</h1>
                    <h4>{post.emotions}</h4>
                    <p>{post.body}</p>
    
            </div>
            ))}
        </div>
    )
}

export default Posts
