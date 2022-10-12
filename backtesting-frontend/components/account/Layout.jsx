import { useEffect } from 'react';
import { useRouter } from 'next/router';

//import { userService } from 'services';

export { Layout };

function Layout({ children }) {
    const router = useRouter();

    useEffect(() => {
        // redirect to home if already logged in
        // if (userService.userValue) {
        //     router.push('/');
        // }

        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return (
        <div className="col-md-12">
            {children}
        </div>
    );
}